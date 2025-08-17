# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hexo static site generator blog using the Icarus theme. Hexo is a Node.js-based static site generator that transforms Markdown files into a static website.

## Common Commands

### Development Commands
```bash
# Start development server (with live reload)
npm run server
# or
hexo server

# Generate static files for production
npm run build
# or
hexo generate

# Clean generated files and cache
npm run clean
# or
hexo clean

# Deploy the site (if deploy config is set)
npm run deploy
# or
hexo deploy
```

### Theme Development Commands
```bash
# Lint theme files (run from themes/icarus directory)
cd themes/icarus && npm run lint
```

## Architecture & Structure

### Core Architecture
- **Static Site Generator**: Hexo (v7.3.0)
- **Theme**: Icarus v6.1.1 (modern, responsive theme)
- **Template Engine**: Inferno/JSX (for theme), EJS and Stylus renderers
- **Content**: Markdown files in `source/_posts/`
- **Output**: Static HTML/CSS/JS in `public/` directory

### Key Directories
- `source/`: Content source files
  - `_posts/`: Blog post markdown files
- `themes/icarus/`: Theme files (separate package with own dependencies)
  - `layout/`: JSX template files
  - `source/`: Theme assets (CSS, JS, images)
  - `include/`: Theme utilities and configurations
- `public/`: Generated static site (do not edit directly)
- `scaffolds/`: Templates for new posts/pages

### Configuration Files
- `_config.yml`: Main Hexo configuration
- `_config.icarus.yml`: Icarus theme configuration (extensive customization options)
- `package.json`: Node.js dependencies and scripts

### Theme Architecture Details
The Icarus theme uses:
- **Inferno** (React-like library) for component rendering
- **Bulma CSS framework** (via bulma-stylus)
- **Stylus** for CSS preprocessing
- **JSX components** in the layout directory
- Modular widget system for sidebars
- Plugin system for features like analytics, comments, etc.

## Content Management

### Creating New Posts
```bash
hexo new post "Post Title"
# Creates source/_posts/Post-Title.md
```

### Post Structure
Posts use YAML front matter with content in Markdown:
```markdown
---
title: Post Title
date: 2023-01-01 12:00:00
categories:
- Category Name
tags:
- tag1
- tag2
---

Post content in Markdown...
```

## Theme Customization

The Icarus theme is highly configurable via `_config.icarus.yml`:
- Supports cyberpunk and default variants
- Configurable widgets (profile, TOC, categories, tags, etc.)
- Plugin system (analytics, comments, sharing, etc.)
- Sidebar layouts and positioning
- SEO and social media integration

When modifying theme files in `themes/icarus/`, run `npm run lint` from that directory to ensure code quality.

## Deployment Notes

- Generated files go to `public/` directory
- Clean before rebuilding: `npm run clean && npm run build`
- The site is configured for deployment but no specific deploy target is set in `_config.yml`

## 一直使用中文对话
## 编写的测试文件使用后记得删除
## 代码中的注释全部使用中文
## 编写完代码都需要进行测试，你可以直接使用控制台命令或者编写 python 脚本或者使用浏览器 mcp 调试
## 多使用 mcp 服务如 context7:获取某个依赖框架的最新文档信息，puppeteer：调用本地浏览器调试前端网页