/// <summary>
/// H5下单API返回json
/// 详细请参考微信支付官方文档: https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_1.shtml
/// <summary>
public class test_api_1_ReturnJson
{

/// <summary>
/// 支付跳转链接 
/// h5_url为拉起微信支付收银台的中间页面，可通过访问该url来拉起微信客户端，完成支付，h5_url的有效期为5分钟。
/// 示例值：https://wx.tenpay.com/cgi-bin/mmpayweb-bin/checkmweb?prepay_id=wx2016121516420242444321ca0631331346&package=1405458241 
/// 可为空: True
/// </summary>
public string h5_url { get; set; }



}
