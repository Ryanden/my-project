import re

from django.conf import settings
from django.db import models


class Store(models.Model):
    PATTERN_HASHTAG = re.compile(r'#(\w+)')

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)
    photos = models.ImageField(upload_to='store', blank=True)
    content = models.TextField(blank=True)

    base_shipping_charge = models.PositiveIntegerField(default=0)
    free_shipping_charge_limit = models.PositiveIntegerField(default=0)
    extra_shipping_charge = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('HashTag', blank=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name='like_stores',
    )

    class Meta:
        ordering = ['-pk']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for tag_name in re.findall(self.PATTERN_HASHTAG, self.content):
            tag, tag_created = HashTag.objects.get_or_create(name=tag_name)
            self.tags.add(tag)

    def __str__(self):
        return f'{self.title}'

    @property
    def content_html(self):
        return re.sub(
            r'#(?P<tag>\w+)',
            '<a href="/stores/tags/\g<tag>">#\g<tag></a>',
            self.content,
        )


class HashTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'HashTag (self.name)'


class Comment(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments',
    )
    _author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    _content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment (store: {self.store.pk}, author: {self.author.username})'

    @property
    def author(self):
        if self.is_deleted:
            return None
        return self._author

    @property
    def content(self):
        if self.is_deleted:
            return '삭제된 댓글입니다'
        return self._content

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


class Inquiry(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='inquiries',
    )
    parent_inquiry = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='inquiries',
    )
    _author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inquiries',
    )
    _content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment (store: {self.store.pk}, author: {self.author.username})'

    @property
    def author(self):
        if self.is_deleted:
            return None
        return self._author

    @property
    def content(self):
        if self.is_deleted:
            return '삭제된 댓글입니다'
        return self._content

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
