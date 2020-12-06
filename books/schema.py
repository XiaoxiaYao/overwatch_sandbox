import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Answer, Category, Question


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "question")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "title", "quiz", "answer")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("id", "question", "answer_text")


class Query(graphene.ObjectType):

    all_quizzes = DjangoListField(QuizzesType)

    # def resolve_all_quizzes(root, info):
    #     return


schema = graphene.Schema(query=Query)
