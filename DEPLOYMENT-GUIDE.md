# Vercel 部署指南

## 🚀 快速部署步骤

### 方法1: 通过Vercel Dashboard（推荐）

1. **登录Vercel**
   - 访问 [vercel.com](https://vercel.com)
   - 使用GitHub账号登录

2. **导入项目**
   - 点击 "New Project"
   - 选择刚才创建的 `deepseekv` GitHub仓库
   - 点击 "Import"

3. **配置项目**
   - **Framework Preset**: 选择 "Other"
   - **Root Directory**: 保持默认（根目录）
   - **Build and Output Settings**: 保持默认

4. **环境变量**（可选）
   - 如果需要，可以添加环境变量
   - 例如：`NODE_ENV=production`

5. **部署**
   - 点击 "Deploy"
   - 等待部署完成（通常1-2分钟）

### 方法2: 使用Vercel CLI

```bash
# 安装Vercel CLI（如果还没安装）
npm i -g vercel

# 在项目目录中
cd D:\zhongyaoruanjian\deepseekv

# 登录Vercel
vercel login

# 部署项目
vercel --prod
```

## ⚙️ Vercel配置说明

项目已包含 `vercel.json` 配置文件，提供以下功能：

### 1. 路由配置
- 根路径 `/` → `deepseek32-landing.html`
- 静态资源正确映射

### 2. HTTP头部优化
- **X-Robots-Tag**: 解决SEO问题
- **安全头部**: XSS保护、内容类型检查等
- **缓存策略**: 不同资源类型的缓存优化

### 3. 性能优化
- 自动压缩（gzip）
- CDN分发
- HTTP/2支持

## 🔧 部署后验证

### 1. 检查部署状态
访问Vercel Dashboard查看部署日志

### 2. 验证SEO设置
```bash
# 检查X-Robots-Tag
curl -I https://your-domain.vercel.app/

# 检查sitemap
curl https://your-domain.vercel.app/sitemap.xml

# 检查robots.txt
curl https://your-domain.vercel.app/robots.txt
```

### 3. 性能测试
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)
- [WebPageTest](https://www.webpagetest.org/)

## 🌐 自定义域名设置

### 1. 在Vercel中添加域名
1. 进入项目设置
2. 点击 "Domains"
3. 添加你的域名

### 2. 配置DNS
Vercel会提供DNS记录，在你的域名提供商中添加：
```
Type: CNAME
Name: @ (或你的子域名)
Value: cname.vercel-dns.com
```

### 3. 更新项目URL
部署后需要更新项目中的硬编码URL：

1. **HTML文件中的链接**：
   ```html
   <link rel="canonical" href="https://your-domain.com">
   ```

2. **sitemap.xml中的URL**：
   ```xml
   <loc>https://your-domain.com/</loc>
   ```

3. **manifest文件中的URL**：
   ```json
   "start_url": "https://your-domain.com/deepseek32-landing.html"
   ```

## 🔄 自动部署

设置完成后，每次你：
1. 向GitHub的main分支推送代码
2. Vercel会自动检测并重新部署
3. 几分钟后新版本就会上线

## 📊 监控和分析

### Vercel Analytics
- 访问量统计
- 性能监控
- 错误追踪

### Google Search Console
1. 添加网站到Google Search Console
2. 提交sitemap
3. 监控索引状态

### 其他工具
- **Screaming Frog**: SEO爬虫分析
- **Ahrefs**: 关键词和反向链接监控
- **Hotjar**: 用户行为分析

## 🐛 常见问题

### Q: 部署后页面样式丢失？
A: 检查CSS路径，确保所有资源使用相对路径

### Q: SEO工具仍显示X-Robots-Tag缺失？
A: 清除缓存后重新检查，Vercel可能需要几分钟更新

### Q: 自定义域名不生效？
A: 检查DNS设置，可能需要等待DNS传播（最多24小时）

### Q: 想要撤销部署？
A: 在Vercel Dashboard中可以回滚到之前的部署版本

## 📞 技术支持

- **Vercel文档**: [vercel.com/docs](https://vercel.com/docs)
- **GitHub Issues**: 项目Issues页面
- **Vercel社区**: [vercel.com/community](https://vercel.com/community)

---

**部署完成后，你的deepseek 3.2落地页将在线上运行！** 🎉