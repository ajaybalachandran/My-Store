from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
class MyView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({'msg': 'Hello World'})


class GoodMorningView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({'msg': 'Good Morning'})


class GoodEveningView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({'msg': 'Good Evening'})


class GoodNightView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({'msg': 'Good Night'})


class AddView(APIView):
  def post(self, request, *args, **kwargs):
    print('here')
    n1 = int(request.data.get('num1'))
    n2 = int(request.data.get('num2'))
    res = n1 + n2
    return Response({'add':res})


class SubView(APIView):
  def post(self, request, *args, **kwargs):
    n1 = int(request.data.get('num1'))
    n2 = int(request.data.get('num2'))
    res = n1 - n2
    return Response({'sub': res})

class Multiplication(APIView):
  def post(self, request, *args, **kwargs):
    n1 = int(request.data.get('num1'))
    n2 = int(request.data.get('num2'))
    res = n1 * n2
    return Response({'mul': f'{n1} * {n2} = {res}'})


class Cube(APIView):
  def post(self, request, *args, **kwargs):
    res = int(request.data.get('num')) ** 3
    return Response({'cube': res})


class Factorial(APIView):
  def post(self, request, *args, **kwargs):
    number = int(request.data.get('num'))

    def fact(n):
      if n == 1:
        return 1
      else:
        return n * fact(n - 1)

    res = fact(number)
    return Response({'factorial': res})


class PrimeOrNot(APIView):
  def post(self, request, *args, **kwargs):
    number = int(request.data.get('num'))

    def prime(n):
      flag = 0
      for num in range(2, n):
        if n % num == 0:
          flag = 1
          break
      if flag == 1 or n < 2:
        return 'Not Prime'
      else:
        return 'Prime'

    res = prime(number)
    return Response({'ans': res})
