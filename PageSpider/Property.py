from PageSpider.Component import Component


class Property:
    name: str  # 参数名称
    chinese_name: str  # 类型名称
    type: str  # 参数类型
    comment: str  # 注释
    nullable: str  # 参数时候可空

    def parse(self) -> str:
        return ("/// <summary>\n"
                "/// {chinese_name}\n"
                "/// {comment}\n"
                "/// 可为空: {nullable}\n"
                "/// </summary>\n"
                ""
                "public {type} {name} {{ get; set; }}").format(chinese_name=self.chinese_name,
                                                               comment=self.comment.replace("\r\n", "\n")
                                                               .replace("\n", "\n/// ")
                                                               .replace("  ", ""),
                                                               nullable=self.nullable, type=self.type, name=self.name)
