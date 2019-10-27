from db.base import Sql


class Provider:

    @staticmethod
    def get_cert_id(args):
        query = """
            SELECT id FROM cert
            where data = '{data}'
                            """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def add_cert(args):
        query = """
            INSERT INTO cert (ip, status)
            VALUES('{ip}', '{status}')
            returning id
        """

        return Sql.exec(query=query, args=args)