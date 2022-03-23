/// <summary>
/// 支付通知API通知参数
/// 详细请参考微信支付官方文档: https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter4_3_5.shtml
/// <summary>
public class test_api_5_NotifyJson
{

/// <summary>
/// 通知ID 
/// 通知的唯一ID 
/// 示例值：EV-2018022511223320873
/// 可为空: True
/// </summary>
public string id { get; set; }

/// <summary>
/// 通知创建时间 
/// 通知创建的时间，遵循rfc3339标准格式，格式为yyyy-MM-DDTHH:mm:ss+TIMEZONE，yyyy-MM-DD表示年月日，T出现在字符串中，表示time元素的开头，HH:mm:ss.表示时分秒，TIMEZONE表示时区（+08:00表示东八区时间，领先UTC 8小时，即北京时间）。例如：2015-05-20T13:29:35+08:00表示北京时间2015年05月20日13点29分35秒。 
/// 示例值：2015-05-20T13:29:35+08:00
/// 可为空: True
/// </summary>
public string create_time { get; set; }

/// <summary>
/// 通知类型 
/// 通知的类型，支付成功通知的类型为TRANSACTION.SUCCESS 
/// 示例值：TRANSACTION.SUCCESS 
/// 可为空: True
/// </summary>
public string event_type { get; set; }

/// <summary>
/// 通知数据类型 
/// 通知的资源数据类型，支付成功通知为encrypt-resource 
/// 示例值：encrypt-resource 
/// 可为空: True
/// </summary>
public string resource_type { get; set; }

/// <summary>
/// 通知数据
/// 通知资源数据
/// json格式，见示例 
/// 可为空: True
/// </summary>
public Resource resource { get; set; }

/// <summary>
/// 回调摘要 
/// 回调摘要 
/// 示例值：支付成功 
/// 可为空: True
/// </summary>
public string summary { get; set; }


 #region 子数据类型

/// <summary>
/// 通知数据
/// 通知资源数据
/// json格式，见示例 
/// <summary>
public class Resource
{

/// <summary>
/// 加密算法类型 
/// 对开启结果数据进行加密的加密算法，目前只支持AEAD_AES_256_GCM 
/// 示例值：AEAD_AES_256_GCM 
/// 可为空: True
/// </summary>
public string algorithm { get; set; }

/// <summary>
/// 数据密文 
/// Base64编码后的开启/停用结果数据密文
/// 示例值：sadsadsadsad
/// 可为空: True
/// </summary>
public string ciphertext { get; set; }

/// <summary>
/// 附加数据 
/// 附加数据 
/// 示例值：fdasfwqewlkja484w
/// 可为空: False
/// </summary>
public string associated_data { get; set; }

/// <summary>
/// 原始类型 
/// 原始回调类型，为transaction 
/// 示例值：transaction
/// 可为空: True
/// </summary>
public string original_type { get; set; }

/// <summary>
/// 随机串 
/// 加密使用的随机串 
/// 示例值：fdasflkja484w
/// 可为空: True
/// </summary>
public string nonce { get; set; }



}

#endregion
}
