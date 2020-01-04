import locale


class Formatter:
    def format_cnpj(self, cnpj):
        return "%s.%s.%s/%s-%s" % (
            cnpj[0:2],
            cnpj[2:5],
            cnpj[5:8],
            cnpj[8:12],
            cnpj[12:14],
        )

    def format_telefone(self, tel):
        if len(tel) > 10:
            return "(%s%s) %s%s%s%s%s-%s%s%s%s" % (
                tel[0],
                tel[1],
                tel[2],
                tel[3],
                tel[4],
                tel[5],
                tel[6],
                tel[7],
                tel[8],
                tel[9],
                tel[10],
            )
        else:
            return "(%s%s) %s%s%s%s-%s%s%s%s" % (
                tel[0],
                tel[1],
                tel[2],
                tel[3],
                tel[4],
                tel[5],
                tel[6],
                tel[7],
                tel[8],
                tel[9],
            )

    def format_cep(self, cep):
        return "%s%s%s%s%s-%s%s%s" % (
            cep[0],
            cep[1],
            cep[2],
            cep[3],
            cep[4],
            cep[5],
            cep[6],
            cep[7],
        )

    def format_brl(self, value):
        locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
        return "R$ " + locale.currency(value, grouping=True, symbol=None)
