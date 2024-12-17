$(function () {
    $('.buzzer').bootstrapSwitch();
    // 스위치 상태 변경 이벤트 핸들러 등록
    $('.buzzer').on('switchChange.bootstrapSwitch', function (event, state) {
        if (state) {
            console.log("스위치가 ON 상태입니다.");
            // 스위치가 켜진 상태일 때 수행할 작업
            socket.emit('set_buzzer', {'data':'on'});
        } else {
            console.log("스위치가 OFF 상태입니다.");
            // 스위치가 꺼진 상태일 때 수행할 작업
            socket.emit('set_buzzer', {'data':'off'});
        }
    });
    socket.emit('get_buzzer', {});
    socket.on('ret_buzzer', function(data) {
        console.log("스위치 상태", data);
        if (data.state) {
            $('.buzzer').bootstrapSwitch('state', true, true);  // 스위치를 ON 상태로 설정
        } else {
            $('.buzzer').bootstrapSwitch('state', false, true); // 스위치를 OFF 상태로 설정
        }
    });    
});