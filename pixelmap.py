import pygame
from pygame import *
from collections import namedtuple

#container to map tiles to IDs
#id is the index of the sprite on the sprite sheet of all object sprites

Object = namedtuple('Object','id')

#each object must be assigned a corresponding value that will be the mapped value of the color used to call it
#on the pixel map

Object_types =
#Wall object obstructs player movement
#if 0, do not place object (place holder)
#room left for other objects to be added

#key is the colour mapped value (1 is white, (256^3)-1 is black)
{
	0: Object('Nothing',0)
	1: Object('Wall',1)
}

class pixelmap(Sprite):
	
	"""
	a class which creates a functional game map from a given pixelmap
	where each pixel's colour corresponds to an object type.

	Must be called with an image file containing one of each object sprite, 
	integer tile width value, and integer tile height value as input.

	Outputs map class to be used for drawing
	"""

	def __init__(self, Image_file, tile_width, tile_height):
		
		#load values into class parameters
		
		self.sprite_sheet = pygame.image.load(Image_file)
		self.object_width = tile_width
		self.object_height = tile_height

		#initialize class parameters to be used later

		self.map_width = None
		self.map_height = None
		self.objects = []

		#add required values for pygame's sprite class

		self.image = None
		self._base_image = None
		self.rect = pygame.Rect(0,0,0,0)

	def get_objects(self):

		"""
		gets the list self._objects, which contains an ordered list of 
		all objects in the room, as read from the pixel map. This function
		is mainly for use in docstring tests

		Requires no input
		"""

		return self._objects[:]

	def load_from_file(self, filename):
		
		"""
		loads the objects from the pixelmap file and puts them into the list 
		self._objects to be drawn. Also sets map parameters not defined in init

		takes a pixel map file as input

		gives an ordered list of objects as output
		"""

		objects = []

		#load in map image and set parameters

		map_image = pygame.image.load(filename)
		self._map_width, self._map_height = map_image.get_size()
		self.rect.w = self._map_width * self._object_width
		self.rect.h = self._map_height *self._object_height

		#go through the image, adding objects

		map_objects = []
		for y in range(self._map_height):
			for x in range(self._map_width):
				objects.append(map_image.get_at_mapped((x,y)))

		return objects

	def tile_coords(self, screen_coords):

		"""
		utility function for snapping to tiled grid: converts screen coordinates
		in pixels to tile coordinates, based on the object default size

		takes in screen coordinates in pixels

		returns tile (object) coordinates
		"""

		x,y = screen_coords
		return (
            math.floor((x - self.rect.left) / self._object_width),
            math.floor((y - self.rect.top) / self._object_height)
        )

	def screen_coords(self, tile_coords):

		"""
		dual of above function; converts tile coordinates to screen coordinates
		in pixels, based on the object default size

		takes in tile (object) coordinates

		returns screen coordinates in pixels
		"""

		x,y = tile_coords
        return (
            x * self._object_width + self.rect.x,
            y * self._object_height + self.rect.y
        )

    def object_exists(self, tile_coords):

    	"""
    	utility function used in doctests and to avoid error messages

    	takes in tile coordinates

    	returns a boolean value of whether the tile is valid
    	"""

    	return not (
    		object_types[self._objects[index]] == 0
            coords[0] < 0 or
            coords[0] >= self._map_width or
            coords[1] < 0 or
            coords[1] >= self._map_height)

    def _tile_position(self, index):
        """
        function used to convert between coordinates (array) and list, as returned by load_from_file

        takes index in list as input

        returns the position of the tile in the array
        """
        return (index % self._map_width, index // self._map_width)





