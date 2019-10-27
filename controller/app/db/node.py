from db.base import Sql


class Provider:

    @staticmethod
    def get_nodes(args):
        query = """
            SELECT id, status FROM Node
                            """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_node(args):
        query = """
            INSERT INTO Node (ip,status)
            VALUES('{ip}', 'running')
            returning id
        """

        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_status(args):
        query_first = """
        UPDATE NODE Set status = 'disabled'
        """
        Sql.exec(query=query_first, args={})
        for ip in args:
            query = """
            UPDATE NODE SET status = 'running'
            where ip = '{ip}'
            """
            Sql.exec(query,args={'ip':ip})
        return "OK"