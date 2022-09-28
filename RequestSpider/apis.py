
def format_apis(api_id, api_name, req_method, url, have_data=True, have_return=True):

    # print(f'****{url}****')
    post_url = url.split('https://api.mch.weixin.qq.com')[-1]
    print(post_url)
    json_base = f'{api_id}ResultJson' if have_return else 'ResultJsonBase'

    if not have_data:
        apis = f"""
            /// <summary>
            /// {api_name}
            /// </summary>
            /// <param name="data">{api_name}需要{req_method}的Data数据</param>
            /// <param name="timeOut"></param>
            /// <returns></returns>
            public async Task<{json_base}> {api_id}Async(int timeOut = Config.TIME_OUT)
            {'{'}
                var url = {api_id}Apis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "{post_url}");
                TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
                return await tenPayApiRequest.RequestAsync<{json_base}>(url, null , timeOut, ApiRequestMethod.{req_method}, checkSign: false);
            {'}'}
        """

    else:
        apis = f"""
            /// <summary>
            /// {api_name}
            /// </summary>
            /// <param name="data">{api_name}需要{req_method}的Data数据</param>
            /// <param name="timeOut"></param>
            /// <returns></returns>
            public async Task<{json_base}> {api_id}Async({api_id}RequestData data, int timeOut = Config.TIME_OUT)
            {'{'}
                var url = {api_id}Apis.GetPayApiUrl(Senparc.Weixin.Config.TenPayV3Host + "{post_url}");
                TenPayApiRequest tenPayApiRequest = new(_tenpayV3Setting);
                return await tenPayApiRequest.RequestAsync<{json_base}>(url, data, timeOut, ApiRequestMethod.{req_method}, checkSign: false);
            {'}'}
        """
    
    return apis