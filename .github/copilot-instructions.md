# Copilot (or LLM) Instructions for Blog Repository

Revised Date: 2025-11-25

## Project Overview
This is a **technical blog built with Quarto**, covering Data Science, ML, Deep Learning, Statistics, and Engineering topics. The site is static-generated from `.qmd` (Quarto Markdown) files and deployed to Netlify.

**Key Tech Stack:**
- **Framework**: Quarto (scientific publishing system)
- **Content**: `.qmd` files (Markdown + embedded code)
- **Build**: `quarto render` → static HTML in `_site/`
- **Deployment**: Netlify
- **Python Environment**: Conda (with specific packages: torch, pandas, numpy, plotly, scipy)

## Content Structure & Navigation

### Hierarchy
```
docs/blog/posts/
├── Math/              # Linear algebra, calculus, optimization
├── Statistics/        # Distributions, hypothesis testing, Bayesian
├── Data_Science/      # CRISP-DM, EDA, feature engineering, MLOps
├── Machine_Learning/  # Classical algorithms, ensembles
├── Deep_Learning/     # CNN, RNN, Transformers, GANs, BERT, GPT, etc.
├── Engineering/       # DevOps, Docker, Git, Python, Infrastructure
│   ├── DevOps/       # Development environments, CI/CD, Kubernetes, monitoring
│   ├── Data_Engineering/  # Apache Airflow, data pipelines
│   ├── Data_Structure/
│   ├── Python/       # Language features, async, decorators
│   ├── Infra/        # Linux, WSL, cloud computing (AWS, Azure, GCP)
│   └── web/
├── RAG/               # Retrieval-Augmented Generation
├── Experimentation/   # A/B testing, causal inference, bandit algorithms
├── Governance/        # Data quality, metadata, compliance
└── Surveilance/       # Monitoring, logging, observability
```

### File Naming & YAML Headers
Each `.qmd` file has a standard YAML header:
```yaml
---
title: "Main Title"
subtitle: "Subtitle (optional)"
description: | 
  Brief description (1-3 sentences explaining content)
categories:
  - Category1
  - Category2
  - Category3
author: Kwangmin Kim
date: MM/DD/YYYY
format: 
  html:
    code-fold: true
    toc: true
    number-sections: true
draft: false
---
```

**Conventions:**
- Use explanatory narrative style (한다 체): avoid polite Korean (합니다, 입니다)
- No emojis in content or responses
- Section numbering enabled (`number-sections: true`)
- Code folding enabled (`code-fold: true`) for readability

## Development Workflows

### Local Preview
```powershell
# Install Quarto and Python dependencies
quarto preview

# Opens live preview at http://localhost:4747
# Auto-reloads on file changes
```

### Building for Deployment
```powershell
quarto render     # Generates _site/ directory
```

### Python Execution in `.qmd`
Files can embed executable Python code blocks. The `_quarto.yml` sets:
```yaml
execute:
  freeze: auto    # Re-render only when source changes
  cache: true
  daemon: true    # Speed up rendering
  eval: false     # Default: don't execute unless specified
```

**To run code**, use code block options:
````markdown
```{python}
#| eval: true
import pandas as pd
print("This executes")
```
````

## Project-Specific Patterns

### Documentation Organization
- Index files (`index.qmd`) list topics with dates and file references
- Topics organized from foundational → advanced
- Cross-references between related topics
- Examples: `docs/blog/posts/Engineering/index.qmd` (comprehensive DevOps learning path)

### DevOps Content Structure (High-Value Reference)
- Pattern: Concept → Installation → Configuration → Practical Workflow

### Code Examples & Demonstrations
- Embed real, executable code snippets
- Use Python/R code blocks with clear annotations
- Plotly for interactive visualizations
- Include error scenarios and troubleshooting

### Multi-Language Support
- Content mainly in Korean (English if specified)
- Maintain consistency across both versions
- Use clear section headers for language separation

## Critical File Locations

### Configuration
- `_quarto.yml` - **Master config**: project type, website settings, navbar, sidebar, Algolia search, deployment settings
- `styles.css` - Custom CSS overrides
- `theme.scss` / `theme-dark.scss` - Light/dark theme definitions
- `blog_requirements.txt` - Python dependencies (torch, plotly, scipy, pandas, etc.)

### Content
- `docs/blog/posts/` - All blog content (organized by category)
- `docs/blog/index.qmd` - Blog landing page with recent posts
- `docs/projects/` - Project case studies (currently inactive, see commented-out sections in `_quarto.yml`)

### Deployment
- `_site/` - Generated static HTML (output directory)
- `.github/` - GitHub workflows (if configured)
- Build: `quarto render` → `_site/` → Netlify auto-deploy on push

## Writing Guidelines for New Content

1. **Choose Category**: Determine which `docs/blog/posts/` subfolder is appropriate
2. **Create File**: Name descriptively, date prefix optional (e.g., `01.git_install.qmd`)
3. **YAML Header**: Follow template above; use clear descriptions
4. **Content Structure**:
   - Start with conceptual overview (narrative style)
   - Build to practical examples
   - Include code blocks with clear context
   - End with troubleshooting or next steps
5. **Code Blocks**: Use language-specific syntax highlighting:
   - ````{python}```` for Python
   - ````{bash}```` or ````{powershell}```` for shell commands
   - ````{r}```` for R code
6. **LaTeX Math**: Inline with `$...$`, display with `$$...$$`
7. **Navigation**: Update parent `index.qmd` if adding new subsection

## Integration Points & Dependencies

### External Services
- **Algolia Search**: Configured in `_quarto.yml` (search indexing)
- **Google Analytics**: ID `G-6W0EKFMWBN` (site metrics)
- **Netlify**: Auto-deploys on GitHub push (`main` branch)
- **GitHub**: Source control, runs Quarto build in CI/CD (if configured)

### Cross-Component Communication
- **Navigation**: Sidebar auto-generated from `_quarto.yml` structure
- **Search**: Quarto auto-indexes all `.qmd` content via Algolia
- **Theming**: Light/dark toggle applied via SCSS (theme.scss / theme-dark.scss)

## Language & Style Rules

### Korean Documentation
- **Use**: Narrative explanatory style (한다 체: 한다, 이다, 하는가, 된다)
- **Avoid**: Polite/formal Korean (경어체: 합니다, 입니다, 합니까)
- **Example**:
  - ✅ `Git은 분산형 버전 관리 시스템이다.`
  - ❌ `Git은 분산형 버전 관리 시스템입니다.`

### General Style
- No emojis in documentation
- Active voice preferred
- Clear, technical language
- Concrete examples over abstractions

## Common AI Agent Tasks

### Add New Blog Post
1. Determine category folder in `docs/blog/posts/`
2. Create `.qmd` file with YAML header (use examples from Git/Poetry as template)
3. Write content in narrative style (설명체)
4. Update parent `index.qmd` with new entry and date
5. Test: `quarto preview`, verify file renders correctly
6. Check: No polite Korean (경어체), clear section numbers

### Update Existing Content
1. Read the file to understand current structure and style
2. Make changes respecting existing patterns (headers, code blocks, formatting)
3. Verify YAML header has required fields (title, description, date, categories)
4. Test: `quarto preview`
5. If modifying navigation structure, update `_quarto.yml` or parent `index.qmd`

### Normalize Documentation Style
- Use `normalizeLanguageStyle.prompt.md` for systematic language conversion
- Replace polite Korean (합니다 → 한다, 입니다 → 이다)
- Preserve markdown formatting, code blocks, and structure
- Verify completeness with final search pass
