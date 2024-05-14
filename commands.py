u1=User.objects.create_user('Vlad')
u2=User.objects.create_user('Kris')
a1=Author.objects.create(user=u1)  
a2=Author.objects.create(user=u2)  
c1=Category.objects.create(name='Спорт')
c2=Category.objects.create(name='Политика') 
c3=Category.objects.create(name='Авто') 
c4=Category.objects.create(name='Кино')
article1 = Post.objects.create(type = 'AR', title = 'First article', text = 'Hello everybody,its my first post', author=a1)
new1 = Post.objects.create(type = 'NE', title = 'First new', text = 'Hello everybody,its my second post', author=a1) 
article2 = Post.objects.create(type = 'AR', title = 'Hello', text = 'Hello, whats up?', author=a2) 


p1= Post.objects.get(pk=1)  
p2= Post.objects.get(pk=2) 
p3= Post.objects.get(pk=3)
c1= Category.objects.get(pk=1) 
c2= Category.objects.get(pk=2) 
c3= Category.objects.get(pk=3)
PostCategory.objects.create(post = p1, category = c1)
PostCategory.objects.create(post = p2, category = c2)
p3.category.add(c1, c3)

com1= Comment.objects.create(user = u1, text= 'nice', post = article1)
com2= Comment.objects.create(user = u2, text= 'Hello', post = article1) 
com3= Comment.objects.create(user = u2, text= 'Hello', post = new1)
com4= Comment.objects.create(user = u1, text= 'Hello', post = article2)

p1.like()
p1.like()
p1.dislike()
p1.rating
p2.like()
p2.like()
p2.dislike()
p2.rating
p3.like()
p3.dislike()
p3.dislike()
p3.rating

com1.like()
com1.rating

a1.update_rating()
a2.update_rating()

Author.objects.order_by('-rating').values_list('user__username', flat=True).first()

Post.objects.all().order_by('rating').values('date_of_creating', 'author__user__username', 'rating', 'title')

best_post = Post.objects.order_by('-rating').first()
best_comments = Comment.objects.filter(post=best_post)
best_comments.values('date', 'user__username', 'rating', 'text')




