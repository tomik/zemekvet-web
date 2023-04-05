module Jekyll
	module ThousandsSeparatedFilter
		def money_thousands_separator(input, separator=",")
			input.to_s.gsub(/(\d)(?=(\d\d\d)+(?!\d))/, "\\1#{separator}")
		end
	end
end

Liquid::Template.register_filter(Jekyll::ThousandsSeparatedFilter)
