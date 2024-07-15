from django.db import models


# Sailor Model
class Sailor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# Profile Model
class Profile(models.Model):
    EMPLOYMENT_STATUS_CHOICES = [
        ('employment', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('student', 'Student'),
        ('freelance', 'Freelance'),
        ('self-employed', 'Self-employed'),
        ('other', 'Other')
    ]

    user = models.OneToOneField(Sailor, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    graduation_year = models.IntegerField(null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.CharField(
        max_length=255,
        choices=EMPLOYMENT_STATUS_CHOICES,
        blank=True,
        null=True
    )
    job_title = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname} - Profile"


# Connection Model
class Connection(models.Model):
    CONNECTION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('blocked', 'Blocked')
    ]

    user = models.ForeignKey(Sailor, on_delete=models.CASCADE, related_name='connections')
    connection_user = models.ForeignKey(Sailor, on_delete=models.CASCADE, related_name='connected_to')
    connection_status = models.CharField(
        max_length=255,
        choices=CONNECTION_STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname} -> {self.connection_user.firstname} {self.connection_user.lastname}"


# Education Model
class Education(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Education at {self.school_name} by {self.user.firstname} {self.user.lastname}"


# Experience Model
class Experience(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Experience at {self.company_name} by {self.user.firstname} {self.user.lastname}"


# Skill Model
class Skill(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Skill: {self.skill_name} by {self.user.firstname} {self.user.lastname}"


# Posts Model
class Post(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.firstname} {self.user.lastname} on {self.post_date}"


# Comments Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.firstname} {self.user.lastname} on {self.comment_date}"


# Likes Model
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like by {self.user.firstname} {self.user.lastname} on {self.like_date}"


# Share Model
class Share(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    share_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Share by {self.user.firstname} {self.user.lastname} on {self.share_date}"


# Group Model
class Group(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Group: {self.group_name} by {self.user.firstname} {self.user.lastname}"


# GroupMember Model
class GroupMember(models.Model):
    user = models.ForeignKey(Sailor, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    membership_status = models.CharField(
        max_length=255,
        choices=[
            ('pending', 'Pending'),
            ('accepted', 'Accepted'),
            ('blocked', 'Blocked')
        ],
        default='pending'
    )

    def __str__(self):
        return f"{self.user.firstname} {self.user.lastname} in group {self.group.group_name} with status {self.membership_status}"
