def format_head(class_name):

    head = f"""
        #region Apache License Version 2.0
        /*----------------------------------------------------------------

        Copyright 2022 Jeffrey Su & Suzhou Senparc Network Technology Co.,Ltd.

        Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file
        except in compliance with the License. You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

        Unless required by applicable law or agreed to in writing, software distributed under the
        License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
        either express or implied. See the License for the specific language governing permissions
        and limitations under the License.

        Detail: https://github.com/JeffreySu/WeiXinMPSDK/blob/master/license.md

        ----------------------------------------------------------------*/
        #endregion Apache License Version 2.0

        /*----------------------------------------------------------------
            Copyright (C) 2022 Senparc
        
            文件名：{class_name}.cs
            文件功能描述：微信支付V3服务商平台接口
            
            创建标识：Senparc - 20220804

        ----------------------------------------------------------------*/

        using Senparc.CO2NET.Helpers;
        using Senparc.CO2NET.Trace;
        using Senparc.Weixin.Entities;
        // TODO: 引入Entities
        // using Senparc.Weixin.TenPayV3.Apis.BasePay;
        // using Senparc.Weixin.TenPayV3.Apis.Entities;
        // using Senparc.Weixin.TenPayV3.Entities;
        // using Senparc.Weixin.TenPayV3.Helpers;
        using System;
        using System.IO;
        using System.Linq;
        using System.Runtime.InteropServices.ComTypes;
        using System.Security.Cryptography;
        using System.Text;
        using System.Threading.Tasks;

        namespace Senparc.Weixin.ServiceProviderTenPayV3.Apis{'{'}
            public class {class_name}{'{'}

                private ISenparcWeixinSettingForTenpayV3 _tenpayV3Setting;

                /// <summary>
                /// 构造函数
                /// </summary>
                /// <param name="senparcWeixinSettingForTenpayV3"></param>
                public {class_name}(ISenparcWeixinSettingForTenpayV3 senparcWeixinSettingForTenpayV3 = null)
                {'{'}
                    _tenpayV3Setting = senparcWeixinSettingForTenpayV3 ?? Senparc.Weixin.Config.SenparcWeixinSetting.TenpayV3Setting;

                {'}'}

                /// <summary>
                /// 返回可用的微信支付地址（自动判断是否使用沙箱）
                /// </summary>
                /// <param name="urlFormat">如：<code>https://api.mch.weixin.qq.com/pay/unifiedorder</code></param>
                /// <returns></returns>
                internal static string GetPayApiUrl(string urlFormat)
                {'{'}
                    //注意：目前微信支付 V3 还没有支持沙箱，此处只是预留
                    return string.Format(urlFormat, Senparc.Weixin.Config.UseSandBoxPay ? "sandboxnew/" : "");
                {'}'}
            """
    
    return head