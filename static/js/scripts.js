document.addEventListener('DOMContentLoaded', function() {
    const feedbackForm = document.getElementById('feedback-form');
    const courseApplicationForm = document.getElementById('course-application-form');
    const modal = document.getElementById('course-application-modal');
    const closeModal = document.getElementsByClassName('close')[0];
    const applyButtons = document.querySelectorAll('.apply-button');
    const logoutButton = document.getElementById('logout-button');
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (logoutButton) {
        logoutButton.addEventListener('click', async function(event) {
            event.preventDefault();
            try {
                const response = await fetch('/api/users/logout/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    }
                });

                if (response.ok) {
                    window.location.href = '/login/';
                } else {
                    console.error('Logout failed');
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('/api/users/login/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ username, password })
                });

                if (response.ok) {
                    window.location.href = '/profile/';
                } else {
                    document.getElementById('login-error').style.display = 'block';
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('login-error').style.display = 'block';
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const password2 = document.getElementById('password2').value;

            if (password !== password2) {
                document.getElementById('register-error').textContent = 'Passwords do not match';
                document.getElementById('register-error').style.display = 'block';
                return;
            }

            try {
                const response = await fetch('/api/users/register/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ username, email, password })
                });

                if (response.ok) {
                    window.location.href = '/login/';
                } else {
                    document.getElementById('register-error').style.display = 'block';
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('register-error').style.display = 'block';
            }
        });
    }

    if (feedbackForm) {
        feedbackForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const description = document.getElementById('description').value;

            try {
                const response = await fetch('/api/feedback/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ description })
                });

                if (response.ok) {
                    document.getElementById('feedback-success').style.display = 'block';
                    document.getElementById('feedback-error').style.display = 'none';
                } else {
                    document.getElementById('feedback-error').style.display = 'block';
                    document.getElementById('feedback-success').style.display = 'none';
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('feedback-error').style.display = 'block';
                document.getElementById('feedback-success').style.display = 'none';
            }
        });
    }

    applyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const courseId = button.getAttribute('data-course-id');
            document.getElementById('course_id').value = courseId;
            modal.style.display = 'block';
        });
    });

    closeModal.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    if (courseApplicationForm) {
        courseApplicationForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const parent_email = document.getElementById('parent_email').value;
            const parent_phone = document.getElementById('parent_phone').value;
            const course_id = document.getElementById('course_id').value;
            const parent_id = document.getElementById('parent_id') ? document.getElementById('parent_id').value : null;

            if (!parent_id) {
                document.getElementById('application-error').style.display = 'block';
                document.getElementById('application-error').textContent = 'You must be a parent to apply for a course.';
                return;
            }

            try {
                const response = await fetch('/api/courses/course-application/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({ parent_email, parent_phone, course_id, parent_id })
                });

                if (response.ok) {
                    window.location.href = '/';
                } else {
                    document.getElementById('application-error').style.display = 'block';
                }
            } catch (error) {
                console.error('Error:', error);
                document.getElementById('application-error').style.display = 'block';
            }
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
