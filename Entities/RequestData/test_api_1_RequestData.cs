/// <summary>
/// H5下单API请求数据
/// 详细请参考微信支付官方文档: https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml
/// <summary>
public class test_api_1_RequestData
{

/// <summary>
/// 服务商应用ID 
/// 服务商申请的公众号appid。 
/// 示例值：wx8888888888888888
/// 可为空: True
/// </summary>
public string sp_appid { get; set; }

/// <summary>
/// 服务商户号 
/// 服务商户号，由微信支付生成并下发 
/// 示例值：1230000109
/// 可为空: True
/// </summary>
public string sp_mchid { get; set; }

/// <summary>
/// 子商户应用ID 
/// 子商户申请的公众号appid。 
/// 
/// 示例值：wxd678efh567hg6999
/// 可为空: False
/// </summary>
public string sub_appid { get; set; }

/// <summary>
/// 子商户号 
/// 子商户的商户号，由微信支付生成并下发。 
/// 示例值：1900000109
/// 可为空: True
/// </summary>
public string sub_mchid { get; set; }

/// <summary>
/// 商品描述 
/// 商品描述 
/// 示例值：Image形象店-深圳腾大-QQ公仔 
/// 可为空: True
/// </summary>
public string description { get; set; }

/// <summary>
/// 商户订单号 
/// 商户系统内部订单号，只能是数字、大小写字母_-*且在同一个商户号下唯一。 
/// 示例值：1217752501201407033233368018 
/// 可为空: True
/// </summary>
public string out_trade_no { get; set; }

/// <summary>
/// 交易结束时间 
/// 订单失效时间，遵循rfc3339标准格式，格式为yyyy-MM-DDTHH:mm:ss+TIMEZONE，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss表示时分秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC8小时，即北京时间）。例如：2015-05-20T13:29:35+08:00表示，北京时间2015年5月20日 13点29分35秒。
/// 订单失效时间是针对订单号而言的，由于在请求支付的时候有一个必传参数prepay_id只有两小时的有效期，所以在重入时间超过2小时的时候需要重新请求下单接口获取新的prepay_id。其他详见时间规则 。 
/// 建议：最短失效时间间隔大于1分钟
/// 示例值：2018-06-08T10:34:56+08:00 
/// 可为空: False
/// </summary>
public string time_expire { get; set; }

/// <summary>
/// 附加数据 
/// 附加数据，在查询API和支付通知中原样返回，可作为自定义参数使用 
/// 示例值：自定义数据   
/// 可为空: False
/// </summary>
public string attach { get; set; }

/// <summary>
/// 通知地址 
/// 通知URL必须为直接可访问的URL，不允许携带查询串，要求必须为https地址。 
/// 格式：URL 
/// 示例值：https://www.weixin.qq.com/wxpay/pay.php 
/// 可为空: True
/// </summary>
public string notify_url { get; set; }

/// <summary>
/// 订单优惠标记 
/// 订单优惠标记 
/// 示例值：WXG 
/// 可为空: False
/// </summary>
public string goods_tag { get; set; }

/// <summary>
/// 结算信息
/// 结算信息
/// 可为空: False
/// </summary>
public Settle_Info settle_info { get; set; }

/// <summary>
/// 订单金额
/// 订单金额信息
/// 可为空: True
/// </summary>
public Amount amount { get; set; }

/// <summary>
/// 优惠功能
/// 优惠功能
/// 可为空: False
/// </summary>
public Detail detail { get; set; }

/// <summary>
/// 场景信息
/// 支付场景描述
/// 可为空: True
/// </summary>
public Scene_Info scene_info { get; set; }


 #region 子数据类型

/// <summary>
/// 结算信息
/// 结算信息
/// <summary>
public class Settle_Info
{

/// <summary>
/// 是否指定分账 
/// 是否指定分账，枚举值 
/// true：是 
/// false：否 
/// 示例值：true
/// 可为空: False
/// </summary>
public bool profit_sharing { get; set; }



}


/// <summary>
/// 订单金额
/// 订单金额信息
/// <summary>
public class Amount
{

/// <summary>
/// 总金额 
/// 订单总金额，单位为分。 
/// 示例值：100 
/// 可为空: True
/// </summary>
public int  total { get; set; }

/// <summary>
/// 货币类型 
/// CNY：人民币，境内商户号仅支持人民币。 
/// 示例值：CNY 
/// 可为空: False
/// </summary>
public string currency { get; set; }



}


/// <summary>
/// 优惠功能
/// 优惠功能
/// <summary>
public class Detail
{

/// <summary>
/// 订单原价 
/// 1、商户侧一张小票订单可能被分多次支付，订单原价用于记录整张小票的交易金额。 
/// 2、当订单原价与支付金额不相等，则不享受优惠。 
/// 3、该字段主要用于防止同一张小票分多次支付，以享受多次优惠的情况，正常支付订单不必上传此参数。 
/// 示例值：608800 
/// 可为空: False
/// </summary>
public int  cost_price { get; set; }

/// <summary>
/// 商品小票ID 
/// 商家小票ID 
/// 示例值：微信123 
/// 可为空: False
/// </summary>
public string invoice_id { get; set; }

/// <summary>
/// 单品列表
/// 单品列表信息 
/// 对于json结构体参数，内层参数的必填属性仅在结构体有传参的情况下才生效，即如果json结构体都不传参，则内层参数必定全部都不传参。
/// 条目个数限制：【1，6000】 
/// 可为空: False
/// </summary>
public Goods_Detail[] goods_detail { get; set; }


 #region 子数据类型

/// <summary>
/// 单品列表
/// 单品列表信息 
/// 对于json结构体参数，内层参数的必填属性仅在结构体有传参的情况下才生效，即如果json结构体都不传参，则内层参数必定全部都不传参。
/// 条目个数限制：【1，6000】 
/// <summary>
public class Goods_Detail
{

/// <summary>
/// 商户侧商品编码 
/// 由半角的大小写字母、数字、中划线、下划线中的一种或几种组成。 
/// 示例值：1246464644 
/// 可为空: True
/// </summary>
public string merchant_goods_id { get; set; }

/// <summary>
/// 微信支付商品编码 
/// 微信支付定义的统一商品编号（没有可不传） 
/// 示例值：1001 
/// 可为空: False
/// </summary>
public string wechatpay_goods_id { get; set; }

/// <summary>
/// 商品名称 
/// 商品的实际名称 
/// 示例值：iPhoneX 256G 
/// 可为空: False
/// </summary>
public string goods_name { get; set; }

/// <summary>
/// 商品数量 
/// 用户购买的数量 
/// 示例值：1
/// 可为空: True
/// </summary>
public int  quantity { get; set; }

/// <summary>
/// 商品单价 
/// 商品单价，单位为分 
/// 示例值：828800 
/// 可为空: True
/// </summary>
public int  unit_price { get; set; }



}

#endregion
}


/// <summary>
/// 场景信息
/// 支付场景描述
/// <summary>
public class Scene_Info
{

/// <summary>
/// 用户终端IP 
/// 用户的客户端IP，支持IPv4和IPv6两种格式的IP地址。
/// 示例值：14.23.150.211 
/// 可为空: True
/// </summary>
public string payer_client_ip { get; set; }

/// <summary>
/// 商户端设备号 
/// 商户端设备号（门店号或收银设备ID）。 
/// 示例值：013467007045764 
/// 可为空: False
/// </summary>
public string device_id { get; set; }

/// <summary>
/// 商户门店信息
/// 商户门店信息 
/// 对于json结构体参数，内层参数的必填属性仅在结构体有传参的情况下才生效，即如果json结构体都不传参，则内层参数必定全部都不传参。
/// 可为空: False
/// </summary>
public Store_Info store_info { get; set; }

/// <summary>
/// H5场景信息
/// H5场景信息
/// 可为空: True
/// </summary>
public H5_Info h5_info { get; set; }


 #region 子数据类型

/// <summary>
/// 商户门店信息
/// 商户门店信息 
/// 对于json结构体参数，内层参数的必填属性仅在结构体有传参的情况下才生效，即如果json结构体都不传参，则内层参数必定全部都不传参。
/// <summary>
public class Store_Info
{

/// <summary>
/// 门店编号 
/// 商户侧门店编号 
/// 示例值：0001 
/// 可为空: True
/// </summary>
public string id { get; set; }

/// <summary>
/// 门店名称 
/// 商户侧门店名称 
/// 示例值：腾讯大厦分店 
/// 可为空: False
/// </summary>
public string name { get; set; }

/// <summary>
/// 地区编码 
/// 地区编码，详细请见省市区编号对照表。 
/// 示例值：440305 
/// 可为空: False
/// </summary>
public string area_code { get; set; }

/// <summary>
/// 详细地址 
/// 详细的商户门店地址 
/// 示例值：广东省深圳市南山区科技中一道10000号 
/// 可为空: False
/// </summary>
public string address { get; set; }



}


/// <summary>
/// H5场景信息
/// H5场景信息
/// <summary>
public class H5_Info
{

/// <summary>
/// 场景类型 
/// 场景类型 
/// 示例值：iOS, Android, Wap 
/// 可为空: True
/// </summary>
public string type { get; set; }

/// <summary>
/// 应用名称 
/// 应用名称 
/// 示例值：王者荣耀
/// 可为空: False
/// </summary>
public string app_name { get; set; }

/// <summary>
/// 网站URL 
/// 网站URL 
/// 示例值：https://pay.qq.com
/// 可为空: False
/// </summary>
public string app_url { get; set; }

/// <summary>
/// iOS平台BundleID 
/// iOS平台BundleID 
/// 示例值：com.tencent.wzryiOS
/// 可为空: False
/// </summary>
public string bundle_id { get; set; }

/// <summary>
/// Android平台PackageName 
/// Android平台PackageName 
/// 示例值：com.tencent.tmgp.sgame
/// 可为空: False
/// </summary>
public string package_name { get; set; }



}

#endregion
}

#endregion
}
