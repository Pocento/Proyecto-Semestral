function confirmarEliminar(id) {
    Swal.fire({
        title: 'Estas seguro??',
        text: "No podras volver a recuperar los datos!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminarlo!'
      }).then((result) => {
          console.log(result)
        if (result.isConfirmed) {
          Swal.fire(
            'Eliminado!',
            'El archivo se ha elminado exitosamente.',
            'success'
          ).then(function() {
              window.location.href = "/eliminar_productos/"+id+"/";
          })
        }
      })
}
