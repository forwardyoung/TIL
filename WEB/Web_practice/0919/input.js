// 1. (id가 text-input인) input 선택
const textInput = document.querySelector('#text-input')
// 2. input 이벤트 등록
// addEverntListner(type, listner)
// 매개변수 type : 수신할 이벤트 유형을 나타내는 대소문자 구분 문자열
// 매개변수 listener : 지정한 이벤트를 수신할 객체 (함수)
textInput.addEventListener('input', function(e) {
    console.log(e) //  웹 콘솔에 메시지를 출력
    // input의 value를 받아오고 싶음
    // input은 이벤트의 대상
    console.log(e.target.value)
})
