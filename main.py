
import shutil
from ApiSpider.ApiSpider import ApiSpider
from PageSpider.PageSpider import PageSpider
from RequestSpider.RequestSpider import RequestSpider
from RequestSpider.RegionSpider import RegionSpider
import os

from RequestSpider.head import format_head

def format_region(target_name_en, region, apis):
    file = f"""
        #region {region}\n
        """
    errs = []
    for api_id,api_name_zh in apis.items():
        
        r, err = RequestSpider.get_apis(api_id, api_name_zh, target_name_en)
        errs.extend(err)
        file += r
        file += '\n'
        # print(r)
    file += f"""
        #endregion\n
    """

    return file, errs

def main():
    if os.path.exists('./Apis/'):
        shutil.rmtree('./Apis/')
        
    os.system("") # 保证转义不失效
    region_info = RegionSpider.get_regions()
    for target_name_zh,regions in region_info.items():
        errs = []

        print("\033[1;31m",end='')
        print('{:*^50}'.format(target_name_zh))
        print('\033[0;0m',end='')
        print(f'> 请输入【\033[1;33m{target_name_zh}\033[0;0m】类名:',end=' ')
        target_name_en = input()

        file = format_head(target_name_en) + '\n'

        for region,apis in regions.items():
            if len(apis)==0:
                continue
            append_file, err = format_region(target_name_en, region, apis)
            file += append_file
            errs.extend(err)
 
        file += '}\n}\n'

        path = f'./Apis/{target_name_en}/'
        
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f'{path}/{target_name_en}.cs', 'w+', encoding='utf8') as f:
            f.write(file)
        
        if len(err)!=0:
            with open(f'{path}/todo.txt', 'w+', encoding='utf8') as f:
                for i in err:
                    f.writelines(i+'\n')
            


if __name__ == '__main__':
    main()
