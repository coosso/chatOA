// 请假信息
interface Fngq1pf6z02ws7 {
    dateStart: Date;
    dateEnd: Date;
    timeStart: string;
    timeEnd: string;
    duration: string;
    timeType: string;
  }
  
  type TableInfo = Fngq1pf6z02ws7;
  
  // 表单信息
  interface FormInfo {
    F60m1pf6z02ws6: number;
    Fngq1pf6z02ws7: TableInfo;
    F63x1pf6z02ws8: string;
    Fy3267hyajyul: string;
  }
  
  
  interface User {
    id: string;
    name: string;
    uid: string;
    avatar: string;
    isDeleted: boolean;
  }
  
  // 处理流程信息
  interface Process {
    types: 1;
    title: "审核人";
    uniqued: "aca99f04de8bff706";
    level: 1;
    select_mode: 0;
    examine_mode: 3;
    settype: 1;
    no_hander: 2;
    users: User[];
  }
  
  export interface AppllyLeave {
    apply_id: number;
    formInfo: FormInfo;
    processInfo: Process[];
  }

  export interface ApplyLeaveChatResponse {
    dateStart: string;
    dateEnd: string;
    duraton: string;
    reason: string;
  }