function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie!== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
// $('#modal_update_button').click(function () {
//   const csrftoken = getCookie('csrftoken');
//   var id = $('#modal-id').val();
//   var data_id = $('#modal-dataid').val();
//   var network = $('#modal-network').val();
//   var plan_type = $('#modal-plantype').val();
//   var amount = $('#modal-amount').val();
//   var size = $('#modal-size').val();
//   var validity = $('#modal-validity').val();
//   console.log(id, data_id, network, plan_type, size, validity);
//   updateItem(csrftoken,id,data_id,network,plan_type,amount,size,validity)
// });

// Function to create a new item
function createItem(data_id,network,plan_type,amount,size,validity) {
    $.ajax({
      url: '/api/data/',
      type: 'POST',
      data: {
          'data_id' : data_id,
          'network' : network,
          'plan_type' : plan_type,
          'amount' : amount,
          'size' : size,
          'validity' : validity,
      },
      success: function (data) {
        console.log('Item created successfully:', data);
      },
      error: function (error) {
        console.error('Error creating item:', error);
      }
    });
  }

  // Function to retrieve all items
  function retrieveItems() {
    $.ajax({
      url: '/api/data/',
      type: 'GET',
      success: function (data) {
          console.log('Items retrieved successfully:', data);
      },
      error: function (error) {
          console.error('Error retrieving items:', error);
      }
    });
  }

  // Function to update an item
  function updateItem(csrftoken,id,data_id,network,plan_type,amount,size,validity) {
    $.ajax({
        url: `/data/${id}/`,  // Replace 1 with the actual item ID
        type: 'PUT',
        header : {
          'Content-Type': 'application/json',
          'X-CSRFToken' : csrftoken,
        },
        data: JSON.stringify({
            'data_id' : data_id,
            'network' : network,
            'plan_type' : plan_type,
            'amount' : amount,
            'size' : size,
            'validity' : validity,
        }),
        success: function (data) {
            alert('Item updated successfully:' + data);
            // console.log('Item updated successfully:', data);
        },
        error: function (error) {
            alert('Errror updating item:' + error);
            // console.error('Error updating item:', error);
        }
    });
}

  // Function to delete an item
  function deleteItem(id) {
    $.ajax({
        url: `/api/networks/${id}`,  // Replace 1 with the actual item ID
        type: 'DELETE',
        success: function () {
            console.log('Item deleted successfully');
        },
        error: function (error) {
            console.error('Error deleting item:', error);
        }
    });
  }

// Uncomment and call the functions as needed
// createItem();
// retrieveItems();
// updateItem();
// deleteItem();