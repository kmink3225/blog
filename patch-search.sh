#!/bin/bash
# post-render hook: listing 검색 대상에 categories, description 추가
sed -i 's/searchColumns: \["listing-date","listing-title","listing-author"\]/searchColumns: ["listing-date","listing-title","listing-author","listing-categories","listing-description"]/' _site/docs/blog/index.html
