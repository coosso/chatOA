const body = {
  formInfo: {
    F60m1pf6z02ws6: 2,
    Fngq1pf6z02ws7: {
      dateStart: "2025/07/18 00:00:00",
      timeStart: "1",
      dateEnd: "2025/07/22 00:00:00",
      timeEnd: "1",
      duration: "120.00",
      timeType: "time",
    },
    F63x1pf6z02ws8: "生病了",
    Fy3267hyajyul: "",
  },
  processInfo: [
    {
      types: 1,
      title: "审核人",
      uniqued: "aca99f04de8bff706",
      level: 1,
      select_mode: 0,
      examine_mode: 3,
      settype: 1,
      no_hander: 2,
      users: [
        {
          id: 1,
          uid: "125f2ee60dec4ef5bc5f91b6182c98e5",
          name: "李恒",
          avatar:
            "https://shmily-album.oss-cn-shenzhen.aliyuncs.com/admin_face/face5.png",
          isDelete: true,
        },
        {
          id: 6,
          uid: "09daef6914264b8990624899cfb1e099",
          name: "顾唯朵",
          avatar:
            "https://shmily-album.oss-cn-shenzhen.aliyuncs.com/admin_face/face5.png",
          isDelete: true,
        },
        {
          id: 8,
          uid: "cef8315304fb4b77b9c8f5447930bd63",
          name: "哈哈哈",
          avatar:
            "https://demo.tuoluojiang.com/uploads/attach/2025/06/3095d202506241428461165.png",
          isDelete: true,
        },
      ],
    },
    {
      types: 1,
      title: "审核人",
      uniqued: "c230cde49138b920b",
      level: 2,
      select_mode: 1,
      examine_mode: 3,
      settype: 4,
      no_hander: 2,
      options: [],
      users: [
        {
          id: "6-1",
          name: "顾唯朵",
          avatar:
            "https://shmily-album.oss-cn-shenzhen.aliyuncs.com/admin_face/face5.png",
          phone: "13289560013",
          job: {
            id: 2,
            name: "副总经理",
            rank_id: 2,
          },
          uid: "09daef6914264b8990624899cfb1e099",
          laravel_through_key: 1,
          user_card: {
            id: 6,
            type: 1,
          },
          value: 6,
          pid: 1,
          label: "顾唯朵",
          type: 1,
          disabled: false,
        },
      ],
    },
  ],
};

fetch("https://demo.tuoluojiang.com/api/ent/approve/apply/save/98", {
  headers: {
    accept: "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    authorization:
      "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vZGVtby50dW9sdW9qaWFuZy5jb20vYXBpL2VudC9jcnVkL2RhdGFiYXNlL2xpc3QiLCJpYXQiOjE3NTIxMTE5NDEsImV4cCI6MTc1Mjk3NTk0MSwibmJmIjoxNzUyMTExOTQxLCJqdGkiOiJ2MlhWZDRaSkx3UkVQY3plIiwic3ViIjoiOCIsInBydiI6ImI5NDYyMjZmNWU0YmJjN2FiN2FkYjQzNjg4MmY5NWE0MGM2ODA1YjEiLCJlbnRJZCI6bnVsbCwidGltZXN0YW1wcyI6MTc1MjExMTk0MX0.j1MTP6h0L1belsSK3apBhkEtQiNMjCqa3yy4d2j4SLU",
    "content-type": "application/json",
    laravel_lang: "zh-cn",
    priority: "u=1, i",
    "sec-ch-ua":
      '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    cookie:
      "tuoluojiang_session=FeQPEKdopG9OUdSXBiRNMhKdXQupwzVi6ilSdtg8; Hm_lvt_ceb81753cc0a2deaf15696dce7bd3d5f=1751870840,1751880650,1752109947,1752476735; Hm_lpvt_ceb81753cc0a2deaf15696dce7bd3d5f=1752476735; HMACCOUNT=BB7DE732BA3513C6; pgv_info==undefined",
    Referer: "https://demo.tuoluojiang.com/admin/user/examine/mine",
  },
  body: JSON.stringify(body),
  method: "POST",
});
