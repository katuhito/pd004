from django.urls import path
#viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewsという名前で利用する
from django.contrib.auth import views as auth_views

#URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

urlpatterns = [
    #サインアップページビューの呼び出し
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    #ログインページの表示
    #[http(s)://<host>/login/]へのアクセスに対して、
    #django.contrib.auth.views.LoginViewをインスタンス化してログインページを表示する
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #ログアウトの実行（ログインと同じ）
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]