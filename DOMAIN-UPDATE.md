# 域名更新指南

## 🔄 需要更新的文件

### 1. HTML文件 (deepseek32-landing.html)
需要更新以下URL：

```html
<!-- 第41行 -->
<link rel="canonical" href="https://deepseekv.pro/">

<!-- 第17行 - Open Graph -->
<meta property="og:url" content="https://deepseekv.pro">

<!-- 第27行 - Twitter Card -->
<meta name="twitter:site" content="@deepseekv_ai">
```

### 2. sitemap.xml
```xml
<!-- 第20行 -->
<url>
    <loc>https://deepseekv.pro/</loc>
    <lastmod>2024-12-06</lastmod>
    ...
</url>
```

### 3. site.webmanifest
```json
{
    "url": "https://deepseekv.pro",
    "scope": "/",
    "start_url": "/deepseek32-landing.html"
}
```

## ✅ 验证清单

- [ ] 域名DNS解析正常
- [ ] HTTPS证书自动签发
- [ ] 页面正常加载
- [ ] SEO工具能正常访问
- [ ] 移动端正常显示
- [ ] PWA功能正常

## 🔍 测试工具

- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [GTmetrix](https://gtmetrix.com/)
- [Google Search Console](https://search.google.com/search-console)

## 📱 营销建议

1. **设置301重定向**（如果有旧域名）
2. **提交sitemap到Google Search Console**
3. **设置Google Analytics**
4. **配置社交媒体分享卡片**

## 🛡️ 安全建议

1. **启用HSTS**：在Vercel中强制HTTPS
2. **设置CSP**：内容安全策略
3. **配置CDN**：全球加速
4. **监控性能**：设置性能监控