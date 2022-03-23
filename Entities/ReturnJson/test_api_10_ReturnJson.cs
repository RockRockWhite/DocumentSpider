/// <summary>
/// 查询单笔退款API返回json
/// 详细请参考微信支付官方文档: https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_10.shtml
/// <summary>
public class test_api_10_ReturnJson
{

/// <summary>
/// 微信支付退款单号
/// 微信支付退款单号
/// 示例值：50000000382019052709732678859
/// 可为空: True
/// </summary>
public string refund_id { get; set; }

/// <summary>
/// 商户退款单号
/// 商户系统内部的退款单号，商户系统内部唯一，只能是数字、大小写字母_-|*@ ，同一退款单号多次请求只退一笔。
/// 示例值：1217752501201407033233368018
/// 可为空: True
/// </summary>
public string out_refund_no { get; set; }

/// <summary>
/// 微信支付订单号
/// 微信支付交易订单号
/// 示例值：1217752501201407033233368018
/// 可为空: True
/// </summary>
public string transaction_id { get; set; }

/// <summary>
/// 商户订单号
/// 原支付交易对应的商户订单号
/// 示例值：1217752501201407033233368018
/// 可为空: True
/// </summary>
public string out_trade_no { get; set; }

/// <summary>
/// 退款渠道
/// 枚举值：
/// ORIGINAL：原路退款
/// BALANCE：退回到余额
/// OTHER_BALANCE：原账户异常退到其他余额账户
/// OTHER_BANKCARD：原银行卡异常退到其他银行卡
/// 示例值：ORIGINAL
/// 可为空: True
/// </summary>
public string channel { get; set; }

/// <summary>
/// 退款入账账户
/// 取当前退款单的退款入账方，有以下几种情况：
/// 1）退回银行卡：{银行名称}{卡类型}{卡尾号}
/// 2）退回支付用户零钱:支付用户零钱
/// 3）退还商户:商户基本账户商户结算银行账户
/// 4）退回支付用户零钱通:支付用户零钱通
/// 示例值：招商银行信用卡0403
/// 可为空: True
/// </summary>
public string user_received_account { get; set; }

/// <summary>
/// 退款成功时间
/// 退款成功时间，当退款状态为退款成功时有返回。
/// 示例值：2020-12-01T16:18:12+08:00
/// 可为空: False
/// </summary>
public string success_time { get; set; }

/// <summary>
/// 退款创建时间
/// 退款受理时间
/// 示例值：2020-12-01T16:18:12+08:00
/// 可为空: True
/// </summary>
public string create_time { get; set; }

/// <summary>
/// 退款状态
/// 退款到银行发现用户的卡作废或者冻结了，导致原路退款银行卡失败，可前往服务商平台-交易中心，手动处理此笔退款。
/// 枚举值：
/// SUCCESS：退款成功
/// CLOSED：退款关闭
/// PROCESSING：退款处理中
/// ABNORMAL：退款异常
/// 示例值：SUCCESS
/// 示例值：SUCCESS
/// 可为空: True
/// </summary>
public string status { get; set; }

/// <summary>
/// 资金账户
/// 退款所使用资金对应的资金账户类型
/// 枚举值：
/// UNSETTLED : 未结算资金
/// AVAILABLE : 可用余额
/// UNAVAILABLE : 不可用余额
/// OPERATION : 运营户
/// BASIC : 基本账户（含可用余额和不可用余额）
/// 示例值：UNSETTLED
/// 可为空: False
/// </summary>
public string funds_account { get; set; }

/// <summary>
/// 金额信息
/// 金额详细信息
/// 可为空: True
/// </summary>
public Amount amount { get; set; }

/// <summary>
/// 优惠退款信息
/// 优惠退款信息
/// 可为空: False
/// </summary>
public Promotion_Detail[] promotion_detail { get; set; }


 #region 子数据类型

/// <summary>
/// 金额信息
/// 金额详细信息
/// <summary>
public class Amount
{

/// <summary>
/// 订单金额
/// 订单总金额，单位为分
/// 示例值：100
/// 可为空: True
/// </summary>
public int total { get; set; }

/// <summary>
/// 退款金额
/// 退款标价金额，单位为分，可以做部分退款
/// 示例值：100
/// 可为空: True
/// </summary>
public int refund { get; set; }

/// <summary>
/// 退款出资账户及金额
/// 退款出资的账户类型及金额信息
/// 可为空: False
/// </summary>
public From[] from { get; set; }

/// <summary>
/// 用户支付金额
/// 现金支付金额，单位为分，只能为整数
/// 示例值：90
/// 可为空: True
/// </summary>
public int payer_total { get; set; }

/// <summary>
/// 用户退款金额
/// 退款给用户的金额，不包含所有优惠券金额
/// 示例值：90
/// 可为空: True
/// </summary>
public int payer_refund { get; set; }

/// <summary>
/// 应结退款金额
/// 去掉非充值代金券退款金额后的退款金额，单位为分，退款金额=申请退款金额-非充值代金券退款金额，退款金额<=申请退款金额
/// 示例值：100
/// 可为空: True
/// </summary>
public int settlement_refund { get; set; }

/// <summary>
/// 应结订单金额
/// 应结订单金额=订单金额-免充值代金券金额，应结订单金额<=订单金额，单位为分
/// 示例值：100
/// 可为空: True
/// </summary>
public int settlement_total { get; set; }

/// <summary>
/// 优惠退款金额
/// 优惠退款金额<=退款金额，退款金额-代金券或立减优惠退款金额为现金，说明详见代金券或立减优惠，单位为分
/// 示例值：10
/// 可为空: True
/// </summary>
public int discount_refund { get; set; }

/// <summary>
/// 退款币种
/// 符合ISO 4217标准的三位字母代码，目前只支持人民币：CNY。
/// 示例值：CNY
/// 可为空: True
/// </summary>
public string currency { get; set; }


 #region 子数据类型

/// <summary>
/// 退款出资账户及金额
/// 退款出资的账户类型及金额信息
/// <summary>
public class From
{

/// <summary>
/// 出资账户类型
/// 下面枚举值多选一。
/// 枚举值：
/// AVAILABLE : 可用余额
/// UNAVAILABLE : 不可用余额
/// 示例值：AVAILABLE
/// 可为空: True
/// </summary>
public string account { get; set; }

/// <summary>
/// 出资金额
/// 对应账户出资金额
/// 示例值：444
/// 可为空: True
/// </summary>
public int amount { get; set; }



}

#endregion
}


/// <summary>
/// 优惠退款信息
/// 优惠退款信息
/// <summary>
public class Promotion_Detail
{

/// <summary>
/// 券ID
/// 券或者立减优惠id
/// 示例值：109519
/// 可为空: True
/// </summary>
public string promotion_id { get; set; }

/// <summary>
/// 优惠范围
/// 枚举值：
/// GLOBAL-全场代金券
/// SINGLE-单品优惠
/// 示例值：SINGLE
/// 可为空: True
/// </summary>
public string scope { get; set; }

/// <summary>
/// 优惠类型
/// 枚举值：
/// COUPON-代金券，需要走结算资金的充值型代金券
/// DISCOUNT-优惠券，不走结算资金的免充值型优惠券
/// 示例值：DISCOUNT
/// 可为空: True
/// </summary>
public string type { get; set; }

/// <summary>
/// 优惠券面额
/// 用户享受优惠的金额（优惠券面额=微信出资金额+商家出资金额+其他出资方金额 ），单位为分
/// 示例值：5
/// 可为空: True
/// </summary>
public int amount { get; set; }

/// <summary>
/// 优惠退款金额
/// 优惠退款金额<=退款金额，退款金额-代金券或立减优惠退款金额为用户支付的现金，说明详见代金券或立减优惠，单位为分
/// 示例值：100
/// 可为空: True
/// </summary>
public int refund_amount { get; set; }

/// <summary>
/// 商品列表
/// 优惠商品发生退款时返回商品信息
/// 可为空: False
/// </summary>
public Goods_Detail[] goods_detail { get; set; }


 #region 子数据类型

/// <summary>
/// 商品列表
/// 优惠商品发生退款时返回商品信息
/// <summary>
public class Goods_Detail
{

/// <summary>
/// 商户侧商品编码
/// 由半角的大小写字母、数字、中划线、下划线中的一种或几种组成
/// 示例值：1217752501201407033233368018
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
/// 示例值：iPhone6s 16G
/// 可为空: False
/// </summary>
public string goods_name { get; set; }

/// <summary>
/// 商品单价
/// 商品单价金额，单位为分
/// 示例值：528800
/// 可为空: True
/// </summary>
public int unit_price { get; set; }

/// <summary>
/// 商品退款金额
/// 商品退款金额，单位为分
/// 示例值：528800
/// 可为空: True
/// </summary>
public int refund_amount { get; set; }

/// <summary>
/// 商品退货数量
/// 单品的退款数量
/// 示例值：1
/// 可为空: True
/// </summary>
public int refund_quantity { get; set; }



}

#endregion
}

#endregion
}
