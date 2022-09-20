const form = document.querySelector('#form')
      form.addEventListener('submit', function(e) {
        e.preventDefault()
        // FormData 객체는 요소를 form
        const formData = new FormData(form)
        console.log(formData) // (파이썬에서의 map object 같은) 별도의 객체여서 조회 X. 반복하면 됨
        // formData.get(name) => 주어진 name 의 해당하는 필드 value를 반환
        console.log(formData.get('password'))
        console.log(formData.get('password_confirmation'))
      })
      