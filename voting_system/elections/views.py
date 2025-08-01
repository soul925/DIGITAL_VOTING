from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render
from .models import Election, Candidate, Vote
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    ElectionSerializer,
    CandidateSerializer,
    VoteSerializer
)
from django.urls import path



User = get_user_model()

# ---------- AUTH VIEWS ----------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                "message": "Login successful",
                "user": UserSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


# ---------- ELECTION CRUD ----------
class ElectionListCreateView(generics.ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ElectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- CANDIDATE CRUD ----------
class CandidateListCreateView(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CandidateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.IsAuthenticated]


# ---------- VOTING ----------
class VoteCreateView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(voter=self.request.user)

def home(request):
    return render(request, "home.html")

def register_page(request):
    return render(request, "register.html")

def login_page(request):
    return render(request, "login.html")

def voterpage(request):
    return render(request, "voter.html")

def managerpage(request):
    return render(request, "manager.html")

def adminpage(request):
    return render(request, "admin.html")

def ladminpage(request):
    return render(request, "ladmin.html")
def lmanagerpage(request):
    return render(request, "lmanager.html")
def lvoterpage(request):
    return render(request, "lvoter.html")