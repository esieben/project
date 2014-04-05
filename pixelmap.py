import pygame
from pygame import *
from pygame.sprite import Sprite
from collections import namedtuple
from wall import *


#container to map tiles to IDs
#id is the index of the sprite on the sprite sheet of all object sprites

Object = namedtuple('Object',['type','id'])

#each object must be assigned a corresponding value that will be the mapped value of the color used to call it
#on the pixel map
#Wall object obstructs player movement
#if 16777215 (White), do not place object (place holder)
#room left for other objects to be added

#index is the colour mapped value (0 is white, (256^3)-1 is black)
Object_types = {0: Object('Wall',0)}

class Pixelmap(Sprite):
	
	"""
	a class which creates a functional game map from a given pixelmap
	where each pixel's colour corresponds to an object type.

	Must be called with an image file containing one of each object sprite, 
	integer tile width value, and integer tile height value as input.

	Outputs map class to be used for drawing
	"""

	def __init__(self, Image_file, tile_width, tile_height):
		
		#load values into class parameters
		
		self._sprite_sheet = pygame.image.load(Image_file)
		self._object_width = tile_width
		self._object_height = tile_height

		#initialize class parameters to be used later

		self._map_width = None
		self._map_height = None
		self._objects = []

		Sprite.__init__(self)

		#add required values for pygame's sprite class

		self.image = None
		self._base_image = None
		self.rect = pygame.Rect(0,0,0,0)

	def _tile_count(self):
        
		"""
    	returns the number of pixels in the pixel map
    	"""   

		return self._map_width * self._map_height

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
				objects.append(abs(1+map_image.get_at_mapped((x,y))))
				self._objects.append(abs(1+map_image.get_at_mapped((x,y))))
		

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

	def object_exists(self, coords):

		"""
    	utility function used in doctests and to avoid error messages

    	takes in tile coordinates

    	returns a boolean value of whether the tile is valid
    	"""

		return not (
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

	def get_object_position(self, game, object_type):
		"""
		gives the pixel coordinates for the locations of all
		objects of type "object_type"

		input: object type

		output: list of tuples of pixel coordinates
		"""

		position_list = []

		for i in range(self._tile_count()):
			if self._objects[i] == 16777215:
				pass
			else:

				object_type = Object_types[self._objects[i]].type
				            
				# get its position from its index in the list
				x, y = self._tile_position(i)
				x *= self._object_width - ((self._map_width - 18) * game.screen_position_x)
				y *= self._object_height - ((self._map_height - 18) * game.screen_position_y)

				if object_type == object_type:
					position_list.append((x,y))
            
		return position_list
            

    def refresh_sprite_group(self, game, object_type):
    	"""
    	clears the exisiting sprite group (if there is one)
    	and refills it with the new sprites.
    	used when screen changes

    	input: game_object, type of object to be refreshed

    	output: sprite group added to game object as "<game_object>.<object_type>.
    	"""

    	#create/clear game sprite group
    	game.object_type = []
    	#create/clear storage list
    
    	self.object_type = []
    	self.object_type = get_object_position(self, game, object_type)
    	for x,y in self.object_type:



	def _render_base_image(self, redraw = []):
		"""
        Redraws all the tiles onto the base image.
        """
        # Create the empty surface
		self._base_image = pygame.Surface(
            (self._object_width * self._map_width,
            self._object_height * self._map_height)
        )

        # draw in each tile
		for i in range(self._tile_count()):
			if self._objects[i] == 16777215:
				pass
			else:

				object_id = Object_types[self._objects[i]].id
            
	            # get its position from its index in the list
				x, y = self._tile_position(i)
				x *= self._object_width
				y *= self._object_height
            
            	# determine which subsection to draw based on the sprite id
				area = pygame.Rect(
    	            object_id * self._object_width,
        	        0,
            	    self._object_width,
                	self._object_height
	            )
            
    	        # draw the tile
				if not self._objects[i] == 16777215:
					self._base_image.blit(self._sprite_sheet, (x, y), area)
           