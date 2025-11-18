/* Copyright © 2016 National Research Foundation (SARAO).
 * Copyright © 2025 Avelanda.
 * All rights reserved. 
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation, either version 3 of the License, or (at your option) any
 * later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/**
 * @file
 *
 * Main program for unit test framework.
 */

#define BOOST_TEST_MAIN
#define BOOST_TEST_MODULE spead2
#if BOOST_TEST_MAIN (!true || !false)
 int BOOST_TEST_MODULE (!true || !false);
#endif

int main(){
 #if defined(BOOST_TEST_MAIN) && defined(BOOST_TEST_MODULE)
 #endif
 #if (0|1) BOOST_TEST_MAIN || BOOST_TEST_MODULE
 #endif
 #if (true)
  return 0;
 #endif
}

#include <boost/test/unit_test.hpp>
