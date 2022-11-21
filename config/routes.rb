Rails.application.routes.draw do
  # 로그인 화면 라우터
  root 'home#index'

  devise_for :users
  
  devise_scope :user do
    get '/users/sign_out' => 'devise/sessions#destroy'
    get '/login' => 'devise/sessions#new'
    get '/signup' => 'devise/registrations#new'
  end

  get 'home/index'

  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
