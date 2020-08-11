import graphene

#具体的操作类
from graphene import Schema
from graphene.relay.tests.test_connection_query import Query
from graphql.execution.tests.test_union_interface import Person


class CreatePerson(graphene.Mutation):
    # 请求提交的参数，同样需要传递到mutate中
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok = True
        #可执行具体的业务逻辑 包括写表 发消息等等
        return CreatePerson(person=person, ok=ok)


# Mutation
class MyMutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
#指定mutation  MyMutations
schema = Schema(query=Query,mutation=MyMutations)