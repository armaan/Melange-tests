#!/usr/bin/env python2.3
#
# Copyright 2012 the Melange authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from melange_functional_actions import FunctionalTestCase

class GSoCFAQTest(FunctionalTestCase):
  """ This test script test the FAQ Page.
  """
  def setUp(self):
    self.init()
    self.setup()
    
  def testGSoCFAQ(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSoC_FAQ")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #click on faq link.
    self.clickOn("xpath", "FAQ")
    self.wait(3)

    #click on users guide link.
    self.clickOn("xpath", "Users_guide_link")
    self.wait(3)
    self.Browser.back()

    #click on students guide link.
    self.wait(3)
    self.clickOn("xpath", "student_guide")
    self.wait(3)
    self.Browser.back()

    #click on mentors guide link.
    self.wait(3)
    self.clickOn("xpath", "Mentor_guide")
    self.wait(3)
    self.Browser.back()

    #click on What is Google Summer of Code link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "What_is_Google_Summer_of_Code_link")
    self.wait(3)
    self.Browser.back()

    #click on What is program timeline link.
    self.wait(3)
    self.clickOn("xpath", "What_is_program_timeline_link")
    self.wait(3)
    self.Browser.back()

    #click on What are the goals of pogram link.
    self.wait(3)
    self.clickOn("xpath", "What_are_the_goals_of_pogram_link")
    self.wait(3)
    self.Browser.back()

    #Check Is_GSoC_a_recruiting_program link.
    self.wait(3)
    self.clickOn("xpath", "Is_GSoC_a_recruiting_program")
    self.wait(3)
    self.Browser.back()

    #Check How_many_expected_orgs link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "How_many_expected_orgs")
    self.wait(3)
    self.Browser.back()

    #Check How_many_expected_students link.
    self.wait(3)
    self.clickOn("xpath", "How_many_expected_students")
    self.wait(3)
    self.Browser.back()

    #Check How_does_program_work link.
    self.wait(3)
    self.clickOn("xpath", "How_does_program_work")
    self.wait(3)
    self.Browser.back()

    #Check When_can_i_apply_for_GSoC link.
    self.wait(3)
    self.clickOn("xpath", "When_can_i_apply_for_GSoC")
    self.wait(3)
    self.Browser.back()

    #Check How_do_evaluations_work link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "How_do_evaluations_work")
    self.wait(3)
    self.Browser.back()

    #Check How_does_a_mentoring_org_apply link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "How_does_a_mentoring_org_apply")
    self.wait(3)
    self.Browser.back()

    #Check How_should_a_mentoring_org_application_look_like link.
    self.wait(3)
    self.clickOn("xpath", "How_should_a_mentoring_org_application_look_like")
    self.wait(3)
    self.Browser.back()    
    
    #Check What_is_an_ideas_list link.
    self.wait(3)
    self.clickOn("xpath", "What_is_an_ideas_list")
    self.wait(3)
    self.Browser.back()    
        
    #Check How_does_a_student_apply link.
    self.wait(3)
    self.clickOn("xpath", "How_does_a_student_apply")
    self.wait(3)
    self.Browser.back()
    
    #Check What_should_a_student_application_look_like link.
    self.wait(3)
    self.clickOn("xpath", "What_should_a_student_application_look_like")
    self.wait(3)
    self.Browser.back()

    #Check Can_a_student_submit_more_than_one_application link.
    self.wait(3)
    self.clickOn("xpath", "Can_a_student_submit_more_than_one_application")
    self.wait(3)
    self.Browser.back()

    #Check Can_student_continue_wok_as_part_of_GSoC link.
    self.wait(3)
    self.clickOn("xpath", "Can_student_continue_wok_as_part_of_GSoC")
    self.wait(3)
    self.Browser.back()

    #Check When_should_start_working_on_application link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "When_should_start_working_on_application")
    self.wait(3)
    self.Browser.back()

    #Check Can_a_student_work_on_more_than_one_project link.
    self.wait(3)
    self.clickOn("xpath", "Can_a_student_work_on_more_than_one_project")
    self.wait(3)
    self.Browser.back()

    #Check Can_group_apply link.
    self.wait(3)
    self.clickOn("xpath", "Can_group_apply")
    self.wait(3)
    self.Browser.back()

    #Check What_if_two_students_are_accepted link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "What_if_two_students_are_accepted")
    self.wait(3)
    self.Browser.back()

    #Check Documentation_proposals link.
    self.wait(3)
    self.clickOn("xpath", "Documentation_proposals")
    self.wait(3)
    self.Browser.back()

    #Check what_is_a_mentoring_organisation link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_is_a_mentoring_organisation")
    self.wait(3)
    self.Browser.back()

    #Check what_is_the_role_of_mentoring_org link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_is_the_role_of_mentoring_org")
    self.wait(3)
    self.Browser.back()

    #Check what_is_the_role_of_organisation_administrator link.
    self.wait(3)
    self.clickOn("xpath", "what_is_the_role_of_organisation_administrator")
    self.wait(3)
    self.Browser.back()

    #Check More_than_one_org_mentor link.
    self.wait(3)
    self.clickOn("xpath", "More_than_one_org_mentor")
    self.wait(3)
    self.Browser.back()

    #Check what_kind_of_mentoring_org_can_apply link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_kind_of_mentoring_org_can_apply")
    self.wait(3)
    self.Browser.back()

    #Check when_will_accepted_orgs_be_announced link.
    self.wait(3)
    self.clickOn("xpath", "when_will_accepted_orgs_be_announced")
    self.wait(3)
    self.Browser.back()

    #Check Are_mentoring_orgs_required_to_use_code_produced link.
    self.wait(3)
    self.clickOn("xpath", "Are_mentoring_orgs_required_to_use_code_produced")
    self.wait(3)
    self.Browser.back()

    #Check Age_restrictions_on_participating link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "Age_restrictions_on_participating")
    self.wait(3)
    self.Browser.back()

    #Check who_is_eligible_to_participate link.
    self.wait(3)
    self.clickOn("xpath", "who_is_eligible_to_participate")
    self.wait(3)
    self.Browser.back()

    #Check Is_my_school_accredited link.
    self.wait(3)
    self.clickOn("xpath", "Is_my_school_accredited")
    self.wait(3)
    self.Browser.back()

    #Check who_is_not_eligible_to_participate link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "who_is_not_eligible_to_participate")
    self.wait(3)
    self.Browser.back()

    #Check Eligibility_requirements_for_mentoring_orgs link.
    self.wait(3)
    self.clickOn("xpath", "Eligibility_requirements_for_mentoring_orgs")
    self.wait(3)
    self.Browser.back()

    #Check I_have_been_accepted_into_accredited_post link.
    self.wait(3)
    self.clickOn("xpath", "I_have_been_accepted_into_accredited_post")
    self.wait(3)
    self.Browser.back()

    #Check I_graduated_in_the_middle_of_program link.
    self.wait(3)
    self.clickOn("xpath", "I_graduated_in_the_middle_of_program")
    self.wait(3)
    self.Browser.back()

    #Check I_have_already_participated_in_GSoC link.
    self.wait(3)
    self.clickOn("xpath", "I_have_already_participated_in_GSoC")
    self.wait(3)
    self.Browser.back()

    #Check Participate_both_as_mentor_and_student link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "Participate_both_as_mentor_and_student")
    self.wait(3)
    self.Browser.back()

    #Check Time_required_to_participate_as_a_student link.
    self.wait(3)
    self.clickOn("xpath", "Time_required_to_participate_as_a_student")
    self.wait(3)
    self.Browser.back()

    #Check Time_required_to_participate_as_a_mentor link.
    self.wait(3)
    self.clickOn("xpath", "Time_required_to_participate_as_a_mentor")
    self.wait(3)
    self.Browser.back()

    #Check How_students_contact_orgs link.
    self.wait(3)
    self.clickOn("xpath", "How_students_contact_orgs")
    self.wait(3)
    self.Browser.back()

    #Check should_students_send_proposals_directly link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "should_students_send_proposals_directly")
    self.wait(3)
    self.Browser.back()

    #Check student_recive_stipend_if_org_does_not_use_code link.
    self.wait(3)
    self.clickOn("xpath", "student_recive_stipend_if_org_does_not_use_code")
    self.wait(3)
    self.Browser.back()

    #Check what_if_there_is_no_org_doing_my_kind_of_wok link.
    self.wait(3)
    self.clickOn("xpath", "what_if_there_is_no_org_doing_my_kind_of_wok")
    self.wait(3)
    self.Browser.back()

    #Check who_owns_the_code link.
    self.wait(3)
    self.clickOn("xpath", "who_owns_the_code")
    self.wait(3)
    self.Browser.back()

    #Check what_licenses_i choose_from link.
    self.wait(3)
    self.clickOn("xpath", "what_licenses_i choose_from")
    self.wait(3)
    self.Browser.back()

    #Check what_language link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_language")
    self.wait(3)
    self.Browser.back()

    #Check where_does_development_occur link.
    self.wait(3)
    self.clickOn("xpath", "where_does_development_occur")
    self.wait(3)
    self.Browser.back()

    #Check How_do_payment_work link.
    self.wait(3)
    self.clickOn("xpath", "How_do_payment_work")
    self.wait(3)
    self.Browser.back()

    #Check I_would_like_to_use_the_work link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "I_would_like_to_use_the_work")
    self.wait(3)
    self.Browser.back()

    #Check Is_it_unusual_for_opensource_developers_to_be_paid link.
    self.wait(3)
    self.clickOn("xpath", "Is_it_unusual_for_opensource_developers_to_be_paid")
    self.wait(3)
    self.Browser.back()

    #Check what_documentation_is_required_from_students link.
    self.wait(3)
    self.clickOn("xpath", "what_documentation_is_required_from_students")
    self.wait(3)
    self.Browser.back()

    #Check what_tax_related_documents_are_required link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_tax_related_documents_are_required")
    self.wait(3)
    self.Browser.back()

    #Check i_am_a_student_in_united_states link.
    self.wait(3)
    self.clickOn("xpath", "i_am_a_student_in_united_states")
    self.wait(3)
    self.Browser.back()

    #Check what_are_program_mailing_list link.
    self.wait(3)
    self.clickOn("xpath", "what_are_program_mailing_list")
    self.wait(3)
    self.Browser.back()

    #Check Is_there_an_irc_channel link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "Is_there_an_irc_channel")
    self.wait(3)
    self.Browser.back()

    #Check what_can_i_do_to_spread_word_about_GSoC link.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "what_can_i_do_to_spread_word_about_GSoC")
    self.wait(3)
    self.Browser.back()

    #Check I_want_to_schedule_a_GSoC_meetup link.
    self.wait(3)
    self.clickOn("xpath", "I_want_to_schedule_a_GSoC_meetup")
    self.wait(3)
    self.Browser.back()

  def tearDown(self):
    self.teardown()
