from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost


class IndexView(ListView):
    """トップページのビュー"""
    #index.htmlをレンダリングする
    template_name = 'index.html'
    #モデルPhotoPostのオブジェクトにorder_by()を適用して投稿日時の降順で並べ替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 6

# class IndexView(TemplateView):
#     """ トップページのビュー"""
#     #index.htmlをレンダリング
#     template_name = 'index.html'

#デコレータにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
#ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    """写真投稿ページのビュー
    PhotoPostForm出て意義だれているモデルとフィールドと連携して投稿データをデータベースに登録する

    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    """
    #forms.pyのPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    #レンダリングするテンプレート
    template_name = "post_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_success')

    def form_valid(self, form):
        """CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う

        parameters:
            form(django.forms.Form):
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        """
        #commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        #投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    """投稿完了ページのビュー

    Attributes:
        template_name: レンダリングするテンプレート
    """
    #post_success.htmlをレンダリングする
    template_name = 'post_success.html'


    

