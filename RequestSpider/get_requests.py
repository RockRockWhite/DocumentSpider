import time
import bs4
from RequestSpider import RequestSpider
from RegionSpider import RegionSpider
from head import format_head
import os

def main():


    region_info = RegionSpider.get_regions()

    for target,regions in region_info.items():
        file = format_head(target) + '\n'
        for region,apis in regions.items():
            if len(apis)==0:
                continue
            file += f"""
            #region {region}\n
            """
            for api_id,api_name in apis.items():
                if api_id in ['chapter4_1_4','chapter4_1_5','wechatpay5_1']:
                    continue
                print(f'正在爬取：{api_id}')
                r = RequestSpider.get_apis(api_id,api_name)
                file += r
                file += '\n'
                # print(r)
            file += f"""
            #endregion\n
            """
        file += '}\n}\n'

        if not os.path.exists('../Apis/'):
            os.makedirs('../Apis/')
        with open(f'../Apis/{target}.cs', 'w+', encoding='utf8') as f:
            f.write(file)

    

    #         # get each region
    #         regions = []
            
    #         #region 特约商户进件接口
    #         /// <summary>
    #         /// 提交申请单
    #         /// </summary>
    #         /// <param name="data">特约商户进件需要POST的Data数据</param>
    #         /// <param name="timeOut"></param>
    #         /// <returns></returns>
    #         public async Task<ApplyResultJson> ApplyAsync(ApplyRequestData data, int timeOut = Config.TIME_OUT)
    #         {
    #             var url = StockApis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "/v3/applyment4sub/applyment/");
    #             TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
    #             return await tenPayApiRequest.RequestAsync<ApplyResultJson>(url, data, timeOut, ApiRequestMethod.POST, checkSign: false);
    #         }

    #         /// <summary>
    #         /// 查询申请单状态:1.通过业务申请编号查询申请状态
    #         /// </summary>
    #         /// <param name="data">查询申请单状态需要的Data数据</param>
    #         /// <param name="timeOut"></param>
    #         /// <returns></returns>
    #         public async Task<ApplyResultJson> GetApplyStatusByBusinessCode(GetApplyStatusRequestData data, int timeOut = Config.TIME_OUT)
    #         {
    #             var url = StockApis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "/v3/applyment4sub/applyment/business_code/" + data.business_code);
    #             TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
    #             return await tenPayApiRequest.RequestAsync<GetApplyStatusResultJson>(url, data, timeOut, ApiRequestMethod.GET, checkSign: false);
    #         }

    #         /// <summary>
    #         /// 查询申请单状态:2.通过申请单号查询申请状态
    #         /// </summary>
    #         /// <param name="data">查询申请单状态需要的Data数据</param>
    #         /// <param name="timeOut"></param>
    #         /// <returns></returns>
    #         public async Task<GetApplyStatusResultJson> GetApplyStatus(GetApplyStatusRequestData data, int timeOut = Config.TIME_OUT)
    #         {
    #             var url = StockApis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "/v3/applyment4sub/applyment/applyment_id/" + data.applyment_id);
    #             TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
    #             return await tenPayApiRequest.RequestAsync<GetApplyStatusResultJson>(url, data, timeOut, ApiRequestMethod.GET, checkSign: false);
    #         }

    #         /// <summary>
    #         /// 修改结算账号
    #         /// </summary>
    #         /// <param name="data">修改结算账号需要POST的Data数据</param>
    #         /// <param name="timeOut"></param>
    #         /// <returns></returns>
    #         public async Task<ReturnJsonBase> ApplyAsync(UpdateAccountInfoRequestData data, int timeOut = Config.TIME_OUT)
    #         {
    #             var url = StockApis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "v3/apply4sub/sub_merchants/" + data.sub_mchid + "/modify-settlement");
    #             TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
    #             return await tenPayApiRequest.RequestAsync<ReturnJsonBase>(url, data, timeOut, ApiRequestMethod.POST, checkSign: false);
    #         }

    #         /// <summary>
    #         /// 查询结算账户API
    #         /// </summary>
    #         /// <param name="data">查询结算账户API需要的Data数据</param>
    #         /// <param name="timeOut"></param>
    #         /// <returns></returns>
    #         public async Task<GetAccountInfoJsonBase> GetAccountInfo(GetAccountInfoRequestData data, int timeOut = Config.TIME_OUT)
    #         {
    #             var url = StockApis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "v3/apply4sub/sub_merchants/" + data.sub_mchid + "/settlement");
    #             TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
    #             return await tenPayApiRequest.RequestAsync<GetAccountInfoJsonBase>(url, data, timeOut, ApiRequestMethod.GET, checkSign: false);
    #         }
    #         #endregion
    #     }
    # }
    # print(head)
    # for i in range(4, 10):
    #     for j in range(1, 20):
    #         print(i,j)
    #         time.sleep(2)
    #         res = RequestSpider.get_apis(f"{i}_Apis",
    #                                  f"https://pay.weixin.qq.com/wiki/doc/apiv3_partner/apis/chapter{i}_{j}_{{index}}.shtml")
    #         print(res)


if __name__ == '__main__':
    main()
