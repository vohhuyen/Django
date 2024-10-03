from django.urls import path
from . import views

app_name = 'polls' 

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:question_id>/', views.detail, name='detail'),  # http://127.0.0.1:8000/polls/1/ sẽ hiển thị chi tiết câu hỏi có question_id = 1.
    path('<int:question_id>/results/', views.results, name='results'),  # http://127.0.0.1:8000/polls/1/results/ sẽ hiển thị kết quả của câu hỏi có question_id = 1.
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Đường dẫn để gửi phiếu bầu
]
