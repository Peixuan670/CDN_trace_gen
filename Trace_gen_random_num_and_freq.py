
import random

class trace_gen:
	"""def __init__(self, file_num, file_freq_list, file_req_num_list, file_offset_list, file_id_list, file_size_list):
		self.file_num = file_num
		self.file_freq_list = file_freq_list
		self.file_req_num_list = file_req_num_list
		self.file_offset_list = file_offset_list
		self.file_id_list = file_id_list
		self.file_size_list = file_size_list"""

	def __init__(self):
		self.file_num = 300			# unique file number
		self.max_time = 5000		# ending time of this trace
		self.min_time = 0			# starting time of this trace


		self.max_num = 100			# max request number for a flow (file ID)
		self.min_num = 1			# min request number for a flow (file ID)
		self.max_inter = 50			# max interval (control request frequency) for a flow (file ID)
		self.min_inter = 1			# min interval (control request frequency) for a flow (file ID)
		self.max_offset = 500		# max starting time (first request) for a flow (file ID)
		self.min_offset = 0			# min starting time (first request) for a flow (file ID)
		self.max_size = 50
		self.min_size = 1
		self.file_freq_list = []	# reques interval list (index is the file index)
		self.file_req_num_list = []	# reques number list (index is the file index)
		self.file_offset_list = []	# reques start time (time offset) list (index is the file index)
		self.file_id_list = []		# file id list (index is the file index)
		self.file_size_list = []	# file size list (index is the file index)

	def set_para(self):
		file_index = 0
		while file_index < self.file_num:
			self.file_freq_list.append(random.randint(self.min_inter,self.max_inter))		# Radom select request interval
			self.file_req_num_list.append(random.randint(self.min_num,self.max_num))		# Radom select request number
			self.file_offset_list.append(random.randint(self.min_offset,self.max_offset))	# Radom select request time offset (starting time)
			self.file_id_list.append(file_index*1000)										# file id = file index * 1000
			self.file_size_list.append(random.randint(self.min_size,self.max_size))			# # Radom select file size

			file_index = file_index + 1
		return

	def print_trace(self):
		file_index = 0
		while file_index < self.file_num:
			req_index = 0
			offset = self.file_offset_list[file_index]
			while req_index < self.file_req_num_list[file_index]:
				req_time = req_index*self.file_freq_list[file_index] + file_offset_list		# request timestamp = request # * interval + time offset (fist request time + interval)
				print ('{} {} {}'.format(req_time, self.file_id_list[file_index], self.file_size_list[file_index]))
				req_index = req_index + 1
			file_index = file_index + 1
		return



if __name__ == '__main__':
    import sys
    new_trace_gen = trace_gen()
    new_trace_gen.set_para()
    new_trace_gen.print_trace()