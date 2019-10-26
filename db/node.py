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
            INSERT INTO Node (nodeId, data)
            VALUES({nodeId}, '{data}')
            returning id
        """

        return Sql.exec(query=query, args=args)