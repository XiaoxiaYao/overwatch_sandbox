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

    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())

    all_questions = graphene.List(QuestionType)

    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info):
        return Question.objects.all()


class CategoryMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)


class Mutation(graphene.ObjectType):

    update_category = CategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
