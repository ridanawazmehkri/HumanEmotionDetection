from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import base64
import binascii
from connection.utils import base64_to_3d_array

@api_view(["POST"])
def process_image(request):
    if request.method == 'POST':
        try:
            # Get the Base64-encoded image data from the request
            image_data = request.data.get('image')
            if not image_data:
                return Response({'success': False, 'message': 'No image data provided.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Decode the Base64 string to binary image data
            decoded_image_data = base64.b64decode(image_data.split(',')[1])
            
            # Process the image data (e.g., save to disk, analyze, etc.)
            
            # Return a success response
            return Response({'message': base64_to_3d_array(image_data)}, status=status.HTTP_200_OK)
        except binascii.Error:
            return Response({'success': False, 'message': 'Invalid Base64 data.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Return an error response if something goes wrong
            return Response({'success': False, 'message': 'Failed to process image.', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Return an error response if the request method is not POST
        return Response({'success': False, 'message': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

