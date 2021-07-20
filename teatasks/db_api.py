from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine, insert


class DbConnector:
    def __init__(self):

        self.engine = create_engine("sqlite:///data/test.db", echo=True)
        # self.base = declarative_base()

        # class Lists(self.base):  # type: ignore
        # __tablename__ = "lists"
        # list_id = Column(Integer, primary_key=True)
        # list_name = Column(String)

        # class Items(self.base):  # type: ignore
        # __tablename__ = "items"
        # item_id = Column(Integer, primary_key=True)
        # list_id = Column(Integer, ForeignKey("lists.list_id"))
        # title = Column(String)
        # content = Column(String)

        # self.items = Items()
        self.metadata = MetaData()
        # init the db
        self.create_db()

    def create_db(self):
        """Creates table objects and instanciates them in the db."""
        self.lists = Table(
            "lists",
            self.metadata,
            Column("list_id", Integer(), primary_key=True),
            Column("list_name", String()),
        )
        self.metadata.create_all(self.engine)

    # create a new todo list in db
    def create_new_todo_list(self, list_name: str) -> None:
        # insert a new row in the Lists Class

        print(f"Inserting {list_name} into the Lists table")
        smt = insert(self.lists).values((1, list_name))
        print(smt)
        connection = self.engine.connect()
        connection.execute(smt)


if __name__ == "__main__":
    connector = DbConnector()
    connector.create_new_todo_list(list_name="hello world")
