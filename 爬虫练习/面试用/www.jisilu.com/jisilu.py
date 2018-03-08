import requests
import json
import openpyxl
import time

headers = {
    'Host':"www.jisilu.cn",
    'Accept':"application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
    'X-Requested-With':"XMLHttpRequest",
    'Cookie':"kbzw__Session=r5hs19knutnqjl1lb5pr1gqmn0; kbz_newcookie=1; Hm_lvt_164fe01b1433a19b507595a43bf58262=1510066129,1510304312,1511100586; Hm_lpvt_164fe01b1433a19b507595a43bf58262=1511101686",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}

def login():
    logindata=open('user','r',encoding='utf-8').read().replace('\r','').replace('\n','')
    logindata=eval(logindata)
    data={
    'user_name':logindata['user_name'],
    'password':logindata['password'],
    'net_auto_login':1,
    '_post_type':'ajax',
    'return_url':'https://www.jisilu.cn'
    }
    session=requests.session()
    session.post('https://www.jisilu.cn/account/ajax/login_process/',data=data).text
    return session

def getdata():
    data={
    'is_search':"0",
    'avolume':"100",
    'bvolume':"100",
    'market':["sh","sz"],
    'ptype':"price",
    'rp':"50",
    'page':"1"
    }
    session=login()
    timestr=str(time.time()).replace('.','')
    html=session.post('https://www.jisilu.cn/data/sfnew/arbitrage_vip_list/?___t=%s'%timestr,data=data).text
    data=json.loads(html)['rows']
    print(data[0])
    write_to_excel(data)
    print('OK')

def write_to_excel(data):
    keys=['fundA_id','fundA_nm','sell1A','increase_rtA','fundA_volume','fundA_amount_increase',
        'fundB_id','fundB_nm','sell1B','increase_rtB','fundB_volume','fundB_amount_increase',
        'abrate','merge_price','est_dis_rt','base_fund_id','base_fund_nm','base_nav','base_est_val',
        'index_nm','idx_incr_rt','asset_ratio','asset_ratio_last','apply_fee','redeem_fee']
    excel=openpyxl.Workbook(write_only=True)
    sheet=excel.create_sheet()
    for item in data:
        cell=[]
        for key in keys:
            try:
                cell.append(item['cell'][key])
            except:
                cell.append('-')
        sheet.append(cell)
    excel.save('result.xlsx')

while True:
    try:
        getdata()
    except Exception as e:
        print(e)
        print('Failed')
        continue
    time.sleep(10)
    break
