class Company < ApplicationRecord
        validates_uniqueness_of :title
end
