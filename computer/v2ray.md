## v2ray的route设置
<details>
<summary>展开查看</summary>
<code>
"routing": {
		"domainStrategy": "IPIfNonMatch",
		"rules": [
			{
				"type": "field",
				"outboundTag": "direct",
				"domain": [
					"geosite:cn",
					"geosite:private",
					"geosite:adobe",
					"geosite:microsoft",
					"geosite:msn",
					"geosite:apple",
					"amazon.com",
					"taobao.com",
					"jd.com",
				]
			},
            {
				"type": "field",
				"outboundTag": "direct",
				"ip": [
					"geoip:private",
					"geoip:cn",
					"ext:geoip-only-cn-private.dat:cn",
					"ext:geoip-only-cn-private.dat:private"
				]
			},
			{
				"type": "field",
				"outboundTag": "blackhole",
				"domain": [
					"geosite:category-ads-all",
					"googeadsserving.cn",
					"baidu.com"
				]
			},
            {
				"type": "field",
				"outboundTag": "blackhole",
				"domain": [
					"geosite:category-ads-all",
					"googeadsserving.cn",
					"baidu.com"
				]
			}
		]
	}


<code>
</details>

### domainStrateg有三种策略
-   `"AsIs"`: 只使用域名(默认值)
-   `"IPIfNonMatch"`: 先用域名,不行再ip
-   `"IPOnDemand"`: 只用ip

## rules
- 一个rule 里面要么是domain要么是ip要么是network不能有两个
- [路由配置 · Project V 官方网站 (v2ray.com)](https://www.v2ray.com/chapter_02/03_routing.html)


## 负载均衡后优先级的问题
[reference](https://github.com/v2fly/v2ray-step-by-step/issues/50)