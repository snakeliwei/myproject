FORMAT: 1A
HOST: https://120.52.121.75:8443

# companyinfo

全国企业公示系统API

## 上传认证cookie，并获得可用省份列表 [/QuerySite]

### 上传认证cookie，并获得可用省份列表 [POST]


+ Request (application/json)

    + Headers

            User-Agent: Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT
            Cookie: 6A9EDB0F-44D4-11E6-8E9F-9C5C8ED178C5

    + Body

            {
                "IMEI": "6A9EDB0F-44D4-11E6-8E9F-9C5C8ED178C5",
                "OS": "iPhone"
            }

+ Response 200 (application/json)

    + Body

            {
                '150000': '1',
                '110000': '1',
                '420000': '1',
                '460000': '1',
                '140000': '1',
                '230000': '1',
                '500000': '1',
                '360000': '1',
                '410000': '1',
                '220000': '1',
                '520000': '1',
                '610000': '1',
                '130000': '1',
                '440000': '1',
                '640000': '1',
                '510000': '1',
                '120000': '1',
                '650000': '1',
                '530000': '1',
                '370000': '1',
                '330000': '1',
                '210000': '1',
                '620000': '1',
                '430000': '1',
                '340000': '1',
                '440300': '1',
                '630000': '1',
                '350000': '1',
                '310000': '1',
                '540000': '1',
                '100000': '1',
                '320000': '1',
                '450000': '1'
            }


## 查询企业简介 [/QuerySummary]

### 根据输入关键字查询企业简介 [POST]


+ Request (application/json)

    + Headers

            User-Agent: Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT
            Cookie: 6A9EDB0F-44D4-11E6-8E9F-9C5C8ED178C5

    + Body

            {
                'AreaCode': '420000'
                'Limit': '50'
                'Page': '1'
                'Q': '武汉百石通达'
            }

+ Response 200 (application/json)

    + Body

            {
                "ERRCODE": "0",
                "RESULT": [
                    {
                        "AREACODE": "420000",
                        "ENTNAME": "武汉百石通达网络科技有限公司",
                        "ENTTYPE": "1130",
                        "ESTDATE": "2013年11月01日",
                        "GSDJLX": "1",
                        "ID": "420000000009042986",
                        "LEREP": "刘晓明",
                        "REGNO": "420100000371917",
                        "REGORG": "武汉市工商行政管理局东湖开发区分局",
                        "UNISCID": "91420100081956142U"
                    }
                ]
            }

## 查询企业信息 [/QueryGSInfo]

### 根据简介中的ID，REGNO，查询企业详细信息 [POST]


+ Request (application/json)

    + Headers

            User-Agent: Mozilla/5.0 (Ios;9.3.1;iPhone;iPhone);Version/1.5.1;ISN_GSXT
            Cookie: 6A9EDB0F-44D4-11E6-8E9F-9C5C8ED178C5

    + Body

            {
                'AreaCode': '420000'
                'EntId': '420000000010030385'
                'EntNo': '420115600365437'
                'Info': 'All'
                'Limit': '50'
                'Page': '1'
                'Q': '武汉百石通达'
            }

+ Response 200 (application/json)

    + Body

            {
                "ERRCODE": "0",
                "RESULT": {
                    "CHECKINFO": [],
                    "EQUINFO": [],
                    "EXCEINFO": [],
                    "LAWINFO": [],
                    "MORTINFO": [],
                    "PUNINFO": [],
                    "RECINFO": {
                        "BRANINFO": [],
                        "LIQINFO": {},
                        "PERINFO": []
                    },
                    "REGINFO": {
                        "BASEINFO": {
                            "ABUITEMCO": "",
                            "APPRDATE": "2016年03月24日",
                            "CBUITEM": "",
                            "COMPFORM": "个人经营",
                            "CONGRO": "",
                            "CONGROUSD": "",
                            "DOM": "武汉市江夏区庙山开发区保利海上五月花1-S09号商铺",
                            "ENTNAME": "武汉市江夏区百石通建材经营部",
                            "ENTTYPE": "个体工商户",
                            "ESTDATE": "2014年11月05日",
                            "ID": "420000000010030385",
                            "LEGCERNO": "422326198004084915",
                            "LEREP": "伍成志",
                            "OPFROM": "",
                            "OPLOC": "武汉市江夏区庙山开发区保利海上五月花1-S09号商铺",
                            "OPSCOPE": "建材批发兼零售；装饰工程施工。(依法须经批准的项目，经相关部门批准后方可开展经营活动）",
                            "OPSTATE": "存续",
                            "OPTO": "",
                            "PARENTNAME": "",
                            "REGCAP": "5",
                            "REGCAPCUR": "",
                            "REGCAPUSD": "0",
                            "REGNO": "420115600365437",
                            "REGORG": "庙山工商所",
                            "REGSTATE": "存续",
                            "TIMESTAMP": "2016年03月24日",
                            "UNISCID": ""
                        },
                        "CHGINFO": [
                            {
                                "ALTAF": "武汉市江夏区百石通建材经营部",
                                "ALTBE": "武汉市江夏区大泉下伍俊昊日用品商行",
                                "ALTDATE": "2016年03月24日",
                                "ALTITEM": "企业名称",
                                "ID": "4420100012109896",
                                "MARPRID": "420000000010030385",
                                "TIMESTAMP": "2016年03月24日"
                            },
                            {
                                "ALTAF": "一般经营范围：建材批发兼零售；装饰工程施工。(依法须经批准的项目，经相关部门批准后方可开展经营活动）；许可经营范围：",
                                "ALTBE": "一般经营范围：个人护理用品、美容护肤品、家居护理用品、厨房用品零售及咨询服务。；许可经营范围：",
                                "ALTDATE": "2016年03月24日",
                                "ALTITEM": "经营范围",
                                "ID": "4420100012109898",
                                "MARPRID": "420000000010030385",
                                "TIMESTAMP": "2016年03月24日"
                            },
                            {
                                "ALTAF": "5",
                                "ALTBE": "1",
                                "ALTDATE": "2016年03月24日",
                                "ALTITEM": "注册资本(或外资中方认缴资本)",
                                "ID": "4420100012109897",
                                "MARPRID": "420000000010030385",
                                "TIMESTAMP": "2016年03月24日"
                            }
                        ],
                        "LEGINFO": []
                    }
                }
            }
