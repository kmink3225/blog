// blog-navigation.js
// This script dynamically generates category-based previous/next blog post navigation and related posts

document.addEventListener('DOMContentLoaded', function() {
  // Only run on blog post pages
  const currentPath = window.location.pathname;
  if (!currentPath.includes('/docs/blog/posts/')) {
    return;
  }

  // Fetch the listings.json file to get all blog posts
  fetch('/listings.json')
    .then(response => response.json())
    .then(data => {
      // Find blog posts and sort by date (descending)
      const allBlogPosts = data.filter(item => item.path && item.path.includes('/docs/blog/posts/'))
        .sort((a, b) => new Date(b.date) - new Date(a.date));

      // Find the current post
      const currentPost = allBlogPosts.find(post => {
        const postPath = post.path.replace(/\.qmd$|\.ipynb$/, '.html');
        return currentPath.endsWith(postPath) || currentPath.includes(postPath);
      });

      if (!currentPost) {
        return; // Current post not found in listings
      }

      // Get current post categories
      const currentCategories = currentPost.categories || [];

      // Filter posts by same category (if categories exist)
      let sameCategoryPosts = allBlogPosts;
      if (currentCategories.length > 0) {
        sameCategoryPosts = allBlogPosts.filter(post => {
          const postCategories = post.categories || [];
          // Check if there's any overlap in categories
          return postCategories.some(cat => currentCategories.includes(cat));
        });
      }

      // Find current post index in the filtered list
      const currentIndex = sameCategoryPosts.findIndex(post => post.path === currentPost.path);

      // Get previous and next posts (in same category)
      const prevPost = currentIndex < sameCategoryPosts.length - 1 ? sameCategoryPosts[currentIndex + 1] : null;
      const nextPost = currentIndex > 0 ? sameCategoryPosts[currentIndex - 1] : null;

      // Create main navigation HTML
      const navHtml = document.createElement('div');
      navHtml.className = 'blog-post-navigation';
      navHtml.style.cssText = 'display: flex; justify-content: space-between; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--bs-border-color);';

      if (prevPost) {
        const prevLink = document.createElement('a');
        prevLink.href = '/' + prevPost.path.replace(/\.qmd$|\.ipynb$/, '.html');
        prevLink.className = 'btn btn-secondary';
        prevLink.innerHTML = '← 이전 글<br><small style="font-size: 0.8em;">' + (prevPost.title || '') + '</small>';
        navHtml.appendChild(prevLink);
      } else {
        navHtml.appendChild(document.createElement('div')); // Spacer
      }

      if (nextPost) {
        const nextLink = document.createElement('a');
        nextLink.href = '/' + nextPost.path.replace(/\.qmd$|\.ipynb$/, '.html');
        nextLink.className = 'btn btn-primary';
        nextLink.innerHTML = '다음 글 →<br><small style="font-size: 0.8em;">' + (nextPost.title || '') + '</small>';
        navHtml.appendChild(nextLink);
      } else {
        navHtml.appendChild(document.createElement('div')); // Spacer
      }

      // Create related posts section (same category, excluding current post)
      const relatedPosts = sameCategoryPosts
        .filter(post => post.path !== currentPost.path)
        .slice(0, 5); // Show up to 5 related posts

      if (relatedPosts.length > 0 && currentCategories.length > 0) {
        const relatedSection = document.createElement('div');
        relatedSection.className = 'related-posts';
        relatedSection.style.cssText = 'margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--bs-border-color);';

        const relatedTitle = document.createElement('h3');
        relatedTitle.textContent = '같은 카테고리의 관련 글 (' + currentCategories.join(', ') + ')';
        relatedSection.appendChild(relatedTitle);

        const relatedList = document.createElement('ul');
        relatedList.style.cssText = 'list-style: none; padding-left: 0;';

        relatedPosts.forEach(post => {
          const listItem = document.createElement('li');
          listItem.style.cssText = 'margin-bottom: 0.5rem;';
          
          const link = document.createElement('a');
          link.href = '/' + post.path.replace(/\.qmd$|\.ipynb$/, '.html');
          link.textContent = post.title || post.path;
          
          if (post.date) {
            const dateSpan = document.createElement('span');
            dateSpan.style.cssText = 'color: #6c757d; margin-left: 0.5rem; font-size: 0.9em;';
            dateSpan.textContent = '(' + new Date(post.date).toLocaleDateString('ko-KR') + ')';
            listItem.appendChild(link);
            listItem.appendChild(dateSpan);
          } else {
            listItem.appendChild(link);
          }
          
          relatedList.appendChild(listItem);
        });

        relatedSection.appendChild(relatedList);

        // Insert related posts section
        const mainContent = document.querySelector('main.content') || document.querySelector('#quarto-content');
        if (mainContent) {
          mainContent.appendChild(relatedSection);
        }
      }

      // Insert main navigation
      const mainContent = document.querySelector('main.content') || document.querySelector('#quarto-content');
      if (mainContent) {
        mainContent.appendChild(navHtml);
      }
    })
    .catch(error => {
      console.error('Error loading blog post listings:', error);
    });
});
