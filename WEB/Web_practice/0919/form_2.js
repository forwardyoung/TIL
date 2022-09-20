  const password = document.querySelector('#password')
  const password_confirmation = document.querySelector('#password_confirmation')
  const login = document.querySelector('#login')

  login.addEventListener('click', function(event){
    if (password.value.length < 8) {
      alert('비밀번호를 8자리 이상 설정해주세요')
    }
    else if (password.value !== password_confirmation.value) {
      alert('비밀번호가 일치하지 않습니다')
    }
    else if (password.value === password_confirmation.value) {
      alert('login success')
    }
  })