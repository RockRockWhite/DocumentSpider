class DataClass:
    name: str  # 类名
    chinese_name: str  # 类型名称
    comment: str  # 注释
    properties: list  # 类型参数
    sub_classes: list  # 子类型

    def parse(self) -> str:
        constructor = ""

        properties_str = ""
        for each in self.properties:
            properties_str += "\n"
            properties_str += each.parse()
            properties_str += "\n"

        sub_classes_str = ""
        for each in self.sub_classes:
            sub_classes_str += "\n"
            sub_classes_str += each.parse()
            sub_classes_str += "\n"
        if self.sub_classes:
            sub_classes_str = " #region 子数据类型\n" + sub_classes_str + "#endregion"

        return ("/// <summary>\n"
                "/// {chinese_name}\n"
                "/// {comment}\n"
                "/// <summary>\n"
                "public class {name}\n"
                "{{\n"
                # "{constructor}"
                # "\n"
                "{properties}\n"
                "\n"
                "{sub_classes}\n"
                "}}\n").format(name=self.name, chinese_name=self.chinese_name,
                               comment=self.comment.replace("\r\n", "\n")
                               .replace("\n", "\n/// ")
                               .replace("  ", ""),
                               constructor=constructor, properties=properties_str, sub_classes=sub_classes_str)


"""    

        /// <summary>
        /// 含参构造函数
        /// </summary>
        /// <param name="combine_appid">合单发起方的appid</param>
        /// <param name="sub_orders">子单信息 最多支持子单条数：10</param>
        public CloseCombineOrderRequestData(string combine_appid, Sub_Order[] sub_orders)
        {
            this.combine_appid = combine_appid;
            this.sub_orders = sub_orders;
        }

        /// <summary>
        /// 合单商户appid	
        /// 合单发起方的appid。
        /// 示例值：wxd678efh567hg6787
        /// </summary>
        public string combine_appid { get; set; }

        /// <summary>
        /// 子单信息数组
        /// 最多支持子单条数：10
        /// </summary>
        public Sub_Order[] sub_orders { get; set; }

        #region 请求数据类型

        /// <summary>
        /// 子单信息
        /// </summary>
        public class Sub_Order
        {
            /// <summary>
            /// 含参构造函数
            /// </summary>
            /// <param name="mchid">子单商户号</param>
            /// <param name="out_trade_no">子单商户订单号</param>
            public Sub_Order(string mchid, string out_trade_no)
            {
                this.mchid = mchid;
                this.out_trade_no = out_trade_no;
            }

            /// <summary>
            /// 无参构造函数
            /// </summary>
            public Sub_Order()
            {
            }

            /// <summary>
            /// 子单商户号
            /// 子单发起方商户号即合单参与方商户号，必须与发起方appid有绑定关系。
            /// 示例值：1900000109
            /// </summary>
            public string mchid { get; set; }
         
            /// <summary>
            /// 子单商户订单号	
            /// 商户系统内部订单号，要求32个字符内，只能是数字、大小写字母_-|*@ ，且在同一个商户号下唯一。
            /// 示例值：20150806125346
            /// </summary>
            public string out_trade_no { get; set; }
        }

        #endregion
"""
