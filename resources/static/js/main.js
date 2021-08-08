$(document).ready(function () {
    var Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000
    });

    $('#report_daterange').daterangepicker({
        locale: {
            format: 'DD.MM.YYYY'
        }
    });

    $('.delete-btn').on('click', function () {
        var $this = $(this);
        console.log($this.attr('href'))
        Swal.fire({
            title: 'Вы уверены, что хотите удалить?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Да',
            cancelButtonText: 'Нет',
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: $this.attr('href'),
                    type: 'POST',
                }).done(function (response) {
                    location.reload();
                }).fail(function (response) {
                    Toast.fire({
                        icon: 'error',
                        title: response.responseText,
                    })
                });
            }
        })

        return false;
    });
});
